# from flask import Flask, render_template, request
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from collections import Counter
import time
import tweepy as tw
import sys
import os
import random

consumer_key=os.environ['oauth_consumer_key']
consumer_secret=os.environ['oauth_consumer_secret']
access_token=os.environ['oauth_token']
access_token_secret=os.environ['oauth_token_secret']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth, wait_on_rate_limit=True)

# A function that generates tweets
def TweetList(authentication, hashtag):
    tweets = []
    for tweet in Cursor(auth_api.search,q=hashtag,count=20, 
    lang='en',since='2018-09-19').items():
      tweets.append("Author: {} \n{} \n{}",tweet.user.screen_name, tweet.text, str(tweet.created_at))
      print(tweets)
    return tweets

foodList = ["rolledicecream","chocolateicecream","strawberryicecream","frozenyogurt","donuts","sorbet","snowcone"]
randFood = random.choice(foodList)
hashtag = "#" + randFood
tweet_list = TweetList(auth_api, hashtag)
random_tweet = random.choice(tweet_list)

# # declaring home page
# app = Flask(__name__)
# @app.route('/', methods = ['GET', 'POST'])

# # defining home page
# def homepage():
#   # returning index.html and list
#   # and length of list to html page
#   return render_template("index.html", random_tweet=random_tweet)

# if __name__ == "__main__":
#     app.run("0.0.0.0","8080", debug = True)

