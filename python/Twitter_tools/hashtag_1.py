import tweepy
import time, datetime
from datetime import timedelta

ckey = '1sfCEr19Px0VMBRJrbEr3FaY1'#keep the quotes, replace this with your consumer key
csecret = 'vKen6YaghHZms7KvsEY0rON9ZaVE6HNrE58Z19o8BPughsoFEm'#keep the quotes, replace this with your consumer secret key
atoken = '3415136763-eJauHqdkJUDip2Bu0jaifoPZDk6bM8TcvnsaCYq'#keep the quotes, replace this with your access token
asecret = 'FWACspFFpDFubPzeiA9b59shqbvlfBkzrDJom5rVszV0z'#keep the quotes, replace this with your access token secret


OAUTH_KEYS = {'consumer_key':ckey, 'consumer_secret':csecret, 'access_token_key':atoken, 'access_token_secret':asecret}
auth = tweepy.OAuthHandler(OAUTH_KEYS['consumer_key'], OAUTH_KEYS['consumer_secret'])
api = tweepy.API(auth)


now = datetime.datetime.now()
today = now.date()
print (".-.-.-.-.-.-.-.-")
print (today)
print (now)

date_today = now.date()
since = date_today - timedelta(days=2)
until = date_today + timedelta(days=1)
print ("sine and until")
print (since)
print (until)
print ("-----------")
counter = 0
counter_old = 0
counterold = 0
print ("Go :")

for tweet in tweepy.Cursor(api.search, q=('nilstesthashtag'), since='2016-09-27', until='2016-09-29 ').items(0):
    print ("start ...")
    counter = counter + 1
    print ("Counter :", counter)
    print ("Counter Old:", counter_old)

    print('Tweet:', tweet.text.encode('utf8'))
    if counter > counter_old:
        print ("one more tweet")
    counter_old = counter
    print("Counter Old ::", counter_old)
    time.sleep(10)
#    counter = 0




#for tweet in tweepy.Cursor(api.search, q=('nilstesthashtag'), since='2016-09-27', until="2016-09-28").items(0):
for tweet in tweepy.Cursor(api.search, q=('nilstesthashtag'), since='2016-09-27', until='2016-09-29 ').items(0):
    if tweet.created_at > now:
        print (today)
        #print ("Name: ",  tweet.author.name.encode('utf8'))
        #print ('Screen-name: ', tweet.author.screen_name.encode('utf8'))
        print ('Tweet created', tweet.created_at)
        print ('Tweet:', tweet.text.encode('utf8'))
        #print ('Location:', tweet.user.location.encode('utf8'))
        #print ('Geo:', tweet.geo)
        print ("Created < than today")
    else:
        print ("Nothing to post")

