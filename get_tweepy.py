import tweepy
import keys 

access_token = keys.ACCESS_TOKEN
access_token_secret = keys.ACCESS_SECRET 
consumer_key = keys.CONSUMER_KEY
consumer_secret = keys.CONSUMER_SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = 'rmiriuk'
sourceTwitter = ['Twitter for iPhone','Twitter for Android','Twitter for iPad','Twitter Web App']

for tweet in tweepy.Cursor(api.user_timeline,id=user).items(2):
    # print(tweet)
    for src in sourceTwitter:
        if tweet.source != src:
            print(tweet.source)

# print(public_tweets[0])



# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)