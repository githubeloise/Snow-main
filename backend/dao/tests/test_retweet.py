


from django.test import TestCase
from .models import User, Tweet
from .service.retweet import create

class UserRetweetTestCase(TestCase):
    def setUp(self):
        
        self.user = User.objects.create_user(username='test_user', password='test_password')
        
        
        self.tweet = Tweet.objects.create(author=self.user, content="Test tweet")

    def test_has_retweeted(self):
        
        self.assertFalse(self.user.has_retweeted(self.tweet))
        
        
        create(self.user, self.tweet)
        self.assertTrue(self.user.has_retweeted(self.tweet))

    def test_create_retweet(self):
        
        initial_retweet_count = self.tweet.retweet_set.count()
        
        
        create(self.user, self.tweet)
        
        
        self.assertEqual(self.tweet.retweet_set.count(), initial_retweet_count + 1)
