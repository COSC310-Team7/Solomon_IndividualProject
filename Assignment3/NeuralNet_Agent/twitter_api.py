# Module imports

# Tweepy module
import tweepy

# Webbrowser module
import webbrowser


def get_tweets(text):

    consumer_key = 'enter your consumer key here'
    consumer_secret_key = 'enter your consumer secret key here'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)

    api = tweepy.API(auth, wait_on_rate_limit=True)

    for tweet in api.search(q=text, lang='en', rpp=2):
        result = f'{tweet.user.name}: {tweet.text}\n\n'

    return result
