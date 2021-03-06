from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    print(instance.user.user_id, filename)
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class TwitterUser(User):
    user_id = models.CharField(max_length=50)


class Credential(models.Model):
    consumer_key = models.CharField(max_length=100)
    consumer_secret = models.CharField(max_length=100)
    access_token_key = models.CharField(max_length=100)
    access_token_secret = models.CharField(max_length=100)
    twitter_user = models.OneToOneField(TwitterUser, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("consumer_key", "consumer_secret", "access_token_key", "access_token_secret")


class Tweet(models.Model):
    tweet_id = models.CharField(max_length=50, unique=True, blank=True, null=True)
    user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    text = models.CharField(max_length=280, default='')
    image1 = models.ImageField(upload_to=user_directory_path, null=True, blank=True, max_length=2000)
    image2 = models.ImageField(upload_to=user_directory_path, null=True, blank=True, max_length=2000)
    image3 = models.ImageField(upload_to=user_directory_path, null=True, blank=True, max_length=2000)
    image4 = models.ImageField(upload_to=user_directory_path, null=True, blank=True, max_length=2000)
    published = models.BooleanField(default=False)
    pub_datetime = models.DateTimeField(null=True, blank=True)
