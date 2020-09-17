 from flask import Flask, render_template, request
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import tweepy as tw
import sys
import os

app = Flask(__name__)
@app.route('/', methods = ['GET', 'POST'])
def sign_in():
    return render_template('index.html')

if __name__ == "__main__":
    app.run("0.0.0.0","8080", debug = True)

consumer_key=os.environ['oauth_consumer_key']
consumer_secret=os.environ['oauth_consumer_secret']
access_token=os.environ['oauth_token']
access_token_secret=os.environ['oauth_token_secret']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)

userID = sys.argv[1]

end_date = datetime.utcnow() - timedelta(days=30)
for tweet in Cursor(auth_api.user_timeline, id=userID).items():
  print(tweet.text + "\n")
  if tweet.created_at < end_date:
    break

