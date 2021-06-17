# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 16:41:04 2021

@author: gferr
"""

from nltk.twitter import Twitter
from nltk.twitter import Query, Streamer, Twitter, TweetViewer, TweetWriter, credsfromfile
from nltk.corpus import twitter_samples
from nltk.twitter.util import json2csv
import pandas as pd

class TwitterAPI():
    oauth = credsfromfile()
    client = Streamer(**oauth)
    client.register(TweetViewer(limit=10))
    client.sample()
    path = BASE_DIR
    def __init__(self,to_screen:True,follow:None,keywords,limit:10):
        self.follow = follow
        self.keywords = keywords
        tw = Twitter.tweets(to_screen = to_screen,follow = follow,keywords = keywords,limit)
    
    def get_twiter(self,keywords):
        client = Query(**oauth)
        tweets = client.search_tweets(keywords,limit)
        tweet = next(tweets)
        return tweet
    
    def get_users(self,*args:None):#by IdUser
        client = Query(**oauth)
        user_info = clinet.user_info_from_id(*args)
        users=[]
        for user in user_info:
            name,followers,following = user_info['name'],user_info['followers_count'],user_info['friends_count']
            users.append(user)
            print (f'{name} {followers} {following}\n')
        return users
    
    def save_tweetes_file(self):    
        client = Streamer(**oauth)
        client.register(TweetWriter(limit=100,subdir='twitter_samples_files'))
        client.statuses.sample()
        
    def get_tweet_JsonFiles(self,json_file2:None):
        if (json_file2 == None):
            all_tweets_samples = twitter_samples.fileids()
            json_file = all_tweet_samples[2] #json file
            tweet_string = twitter_samples.strings(json_file)    
            return tweet_string
        tweet_string = json_file2
        return tweet_string
    
    def tokenize_tweets(self,string_tweet):
        toked_tweet = twitter_sample.tokenized(string_tweet)
        return toked_tweet
    
    def convert_csv_tweet_file(self,input_file,args=['created_at', 'favorite_count','id', 'in_reply_to_status_id', 'in_reply_to_user_id', 'retweet_count','text', 'truncated', 'user.id']):
        with open(input_file) as file:
            json2csv(file,path+'tweets_text.csv',args)
            return open(path+'tweets_text.csv','r').readlines()
    
    def read_csv_tweets(self,filepath,*args):
        tw = pd.read_csv(filepath,header='tweets',index_col=1,encoding='utf-8',dtype=32).head()        
        return tw
    
    def get_tweet_by_id(self,filepath,tw_id):
        ids = str(tw_id)
        ids = StringIO(ids)
        client = Query(**oauth)
        hydrated = client.expand_tweetids(ids_f)
        tw = read_csv_tweets(filepath)
        for i in hydrated:
            yield tw.loc[tw['user.id'] == i]['text']
        
    