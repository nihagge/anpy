import tweepy
import time
from datetime import timedelta

# from python.Twitter_tools.hashtag_1 import counter_old

ckey = '1sfCEr19Px0VMBRJrbEr3FaY1'#keep the quotes, replace this with your consumer key
csecret = 'vKen6YaghHZms7KvsEY0rON9ZaVE6HNrE58Z19o8BPughsoFEm'#keep the quotes, replace this with your consumer secret key
atoken = '3415136763-eJauHqdkJUDip2Bu0jaifoPZDk6bM8TcvnsaCYq'#keep the quotes, replace this with your access token
asecret = 'FWACspFFpDFubPzeiA9b59shqbvlfBkzrDJom5rVszV0z'#keep the quotes, replace this with your access token secret
OAUTH_KEYS = {'consumer_key':ckey, 'consumer_secret':csecret, 'access_token_key':atoken, 'access_token_secret':asecret}
auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
api = tweepy.API(auth)

results = api.search(q="#cancer", since='2016-09-26', until='2016-09-30 ')

for result in results:
    print (result)
    print (tweet.id_str)
    print ("Name: ",  tweet.author.name.encode('utf8'))




#print (results)
#print (tweet.screen_name)
#print (results_1)
#print("---")


#for result in results:
#    print (results.text)
