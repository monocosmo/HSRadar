import re
import csv
import pandas as pd
import tweepy
from tweepy import OAuthHandler

# Apply for a Twitter Developer account to acquire Twitter API key
consumer_key = 'PASTE YOUR OWN KEY HERE'
consumer_secret = 'PASTE YOUR OWN KEY HERE'
access_token = 'PASTE YOUR OWN KEY HERE'
access_token_secret = 'PASTE YOUR OWN KEY HERE'
# create OAuthHandler object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# set access token and secret
auth.set_access_token(access_token, access_token_secret)
# create tweepy API object to fetch tweets
api = tweepy.API(auth)

keyword = 'COVID' # Change the keyword
data_until = '2020-04-13' # Change the valid date

# remove the emojis from the contents of the text.
def data_clean(string):
    emoji = re.compile("["
                       u"\U0001F600-\U0001F64F"  # emoticons
                       u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                       u"\U0001F680-\U0001F6FF"  # transport & map symbols
                       u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                       u"\U00002702-\U000027B0"
                       "]+", flags=re.MULTILINE)
    res = emoji.sub(r'', string)
    res = re.sub(r"^https?:\/\/.*[\r\n]*", "", res, flags=re.MULTILINE)  # remove the url
    res = re.sub('[@#]', '', res)  # remove @people and #hashtag
    return res

# collect tweets
tweets = tweepy.Cursor(api.search, q = keyword, lang = "en",
                       until = data_until, tweet_mode='extended').items(5000)

# collect tweet text
data = []
for tweet in tweets:
    data.append(tweet.full_text)

# data cleaning
cleaned_tweet = []
for tweet in data:
    cleaned_tweet.append(data_clean(tweet))

data = pd.DataFrame(set(cleaned_tweet))
data.to_csv('./data/en2.csv', index=False)
