from time import sleep
from gpiozero import PWMLED
from twython import TwythonStreamer

hashtags = {
    '#yes': {
        'led': PWMLED(18),
        'count': 0,
    },
    '#no': {
        'led': PWMLED(15),
        'count': 0,
    },
}

# Twitter application authentication
APP_KEY = '3415136763'
APP_SECRET = 'FWACspFFpDFubPzeiA9b59shqbvlfBkzrDJom5rVszV0z'
OAUTH_TOKEN = '1sfCEr19Px0VMBRJrbEr3FaY1'
OAUTH_TOKEN_SECRET = 'vKen6YaghHZms7KvsEY0rON9ZaVE6HNrE58Z19o8BPughsoFEm'

# Setup callbacks from Twython Streamer
class BlinkyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            for hashtag in hashtags:
                if hashtag in data['text']:
                    if hashtags[hashtag]['count'] < 100:
                        hashtags[hashtag]['count'] += 1
                    hashtags[hashtag]['led'].value = hashtags[hashtag]['count'] / 100
                    print(hashtag, hashtags[hashtag]['count'])


# Create streamer
stream = BlinkyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
terms = ','.join(hashtags)  # comma separate hashtags from dictionary
stream.statuses.filter(track=terms)