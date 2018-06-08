from django.db.models.signals import post_save
from django.dispatch import receiver
from tw.models import Credential, Tweet, TwitterUser
from tastypie.models import ApiKey
import twitter


@receiver(post_save, sender=Credential)
def credentials_handler(sender, instance, **kwargs):
    api = twitter.Api(instance.consumer_key,
            instance.consumer_secret,
            instance.access_token_key,
            instance.access_token_secret)
    creds = api.VerifyCredentials()
    user, created = TwitterUser.objects.get_or_create(
            user_id=creds.id, username=creds.screen_name)
    if created:
        instance.twitter_user = user
        instance.save()
        ApiKey.objects.create(user=user)

@receiver(post_save, sender=Tweet)
def tweet_handler(sender, instance, **kwargs):
    from tw.celery import twittear
    twittear.delay(instance.id)
