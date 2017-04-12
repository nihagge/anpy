#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This scripts checks the number of tweets depending on the hashtag. If the number of tweets increases, the function
BLINK() will be fired ;)
I wrote this one to feed my newpixel wheel
"""
import tweepy
import time

CONSUMER_KEY = '1sfCEr19Px0VMBRJrbEr3FaY1'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'vKen6YaghHZms7KvsEY0rON9ZaVE6HNrE58Z19o8BPughsoFEm'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '3415136763-eJauHqdkJUDip2Bu0jaifoPZDk6bM8TcvnsaCYq'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'FWACspFFpDFubPzeiA9b59shqbvlfBkzrDJom5rVszV0z'#keep the quotes, replace this with your access token secret

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

SEARCH_TAG = "#vcfb" # -> search for want you want. But keep in mind : the search request can take while
STRING=[]
COUNTER = 0
COUNTER_MASTER = 0

def BLINK(val):
    for I in range(val):
        print ("BLINK BLINK BLINK BLINK BLINK BLINK BLINK BLINK")
        print ("CHECK_ID: ", CHECK_ID)

while True:
    search_result = tweepy.Cursor(api.search, q=SEARCH_TAG).items()
    print ("---")
    for tweet in search_result:
        CHECK_ID = tweet.id_str
        if CHECK_ID not in STRING:
            STRING.append(tweet.id_str)
        COUNTER = len(STRING)
    print (STRING)
    if COUNTER_MASTER < COUNTER:
        BLINK(10)
    COUNTER_MASTER = COUNTER
    time.sleep(10) # -> take care of penetration the Twitter API
    print ("Next Round ...")



