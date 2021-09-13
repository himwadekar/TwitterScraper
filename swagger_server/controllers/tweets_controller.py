import tweepy
import twitterscraper.utills.authentication as auth

def tweets_using_hashtag(hashtag, number_of_tweets = 30):  # noqa: E501

    api = auth.authenticate()
    response = []
    for tweet in tweepy.Cursor(api.search, q="#".format(hashtag), lang="en").items(number_of_tweets):
        response.append({str(tweet.created_at): tweet.text})
    return response


def user_tweets(userID, number_of_tweets = 30):  # noqa: E501
    api = auth.authenticate()
    user = userID
    response = []
    tweets = api.user_timeline(screen_name = user, count = number_of_tweets , include_rts = False, tweet_mode = 'extended')
    for info in tweets:
        response.append({"TweetID:{}.".format(info.id):{str(info.created_at) : info.full_text}})
    return response
