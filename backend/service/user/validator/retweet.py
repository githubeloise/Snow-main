# service/retweet.py

from .models import Retweet

def create(user, tweet):
    retweet, created = Retweet.objects.get_or_create(user=user, tweet=tweet)
    return retweet
