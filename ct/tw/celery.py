from __future__ import absolute_import, unicode_literals
import os
from datetime import datetime
from celery import Celery
# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ct.settings')

app = Celery('proj')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task
def twittear(tweet_local_id):
    from twitter import Api
    from tw.models import Credential, Tweet
    tweet = Tweet.objects.get(id=tweet_local_id)
    if tweet.tweet_id is None:
        twitter_user = tweet.user
        user_credentials = Credential.objects.get(twitter_user=twitter_user)
        api = Api(user_credentials.consumer_key, user_credentials.consumer_secret, 
                user_credentials.access_token_key, user_credentials.access_token_secret)
        files = []
        if tweet.image1:
            files.append(tweet.image1.path)
        if tweet.image2:
            files.append(tweet.image2.path)
        if tweet.image3:
            files.append(tweet.image3.path)
        if tweet.image4:
            files.append(tweet.image4.path)
        result = api.PostUpdate(status=tweet.text, media=files)
        tweet.tweet_id = result.id
        tweet.pub_datetime = datetime.utcfromtimestamp(result.created_at_in_seconds)
        tweet.published = True
        tweet.save()
