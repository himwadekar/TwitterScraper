import tweepy
from twitterscraper.utills.env import CONSUMER_KEY, CONSUMER_SECRET


def authenticate():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    authenticated = tweepy.API(auth)
    return authenticated