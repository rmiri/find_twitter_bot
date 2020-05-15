import tweepy
import keys 



access_token = keys.ACCESS_TOKEN
access_token_secret = keys.ACCESS_SECRET 
consumer_key = keys.CONSUMER_KEY
consumer_secret = keys.CONSUMER_SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

user = 'jultaijt'

for tweet in tweepy.Cursor(api.user_timeline,id=user).items(50):
    # print(tweet.text)
    if tweet.source != 'Twitter for iPhone':
        if tweet.source != 'Twitter for Android':
            # print(tweet)
            print(tweet.source)

# print(public_tweets[0])

