# Module imports

# Tweepy module
import tweepy


def get_tweets(text):

    consumer_key = 'Add yours'
    consumer_secret_key = 'Add yours'

    access_token = 'Add yours'
    access_token_secret = 'Add yours'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True)

    for tweet in api.search(q=text, lang='en', rpp=2):
        result = f'{tweet.user.name}: {tweet.text}\n\n'

    return result
