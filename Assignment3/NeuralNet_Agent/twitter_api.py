# Module imports

# Tweepy module
import tweepy

# Webbrowser module
import webbrowser


def get_tweets(text):

    fake = 'dummy result'

    consumer_key = 'add yours'
    consumer_secret_key = 'add yours'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)

    api = tweepy.API(auth, wait_on_rate_limit=True)

    for tweet in api.search(q=text, lang='en', rpp=2):
        result = f'{tweet.user.name}: {tweet.text}\n\n'

    return result
