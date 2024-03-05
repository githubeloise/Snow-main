# service/tweet.py

from .models import Tweet

def get_tweet(tweet_id):
    try:
        return Tweet.objects.get(id=tweet_id)
    except Tweet.DoesNotExist:
        return None

# Add more tweet-related functions as needed
