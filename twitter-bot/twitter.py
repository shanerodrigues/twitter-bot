import tweepy
import time

auth = tweepy.OAuthHandler('consumerAPI #1','consumerAPI #2')
auth.set_access_token('access token #1','access token #2')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

'''user = api.me()

for follower in tweepy.Cursor(api.followers).items():
    print(follower.name)

search = 'Warne'
nrTweets = 10

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('Tweet Liked')
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
'''
search = 'Warne'
nrTweets = 10

# Retweet Shane Warne
for tweet in tweepy.Cursor(api.user_timeline, id="ShaneWarne").items(nrTweets):
    try:
        print('Warnie Retweeted')
        tweet.retweet()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break