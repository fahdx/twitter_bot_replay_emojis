
import tweepy
import random as r
from http.client import IncompleteRead
import time

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()
        self.counter=0

    def on_status(self, tweet):

        txt = "\U0001F337 \U0001F338 \U0001F490 \U0001F3F5 \U0001F339 \U0001F339 \U0001F33A \U0001F33B \U0001F33C"
        print(self.counter)
        self.counter+=1


        twet = ""
        flowers_emoji = txt.split(" ")

        for f in range(52):
            num = r.randint(0, 7)
            twet += flowers_emoji[num]
    #str(tweet.user.screen_name)+
        print(api.update_status("@"+str(tweet.user.screen_name)+twet , in_reply_to_status_id=tweet.id))

        print(tweet.user.name)

        print('=----------------------------------=')

    def on_error(self, status):
        print("Error detected")
        print(status)

# Authenticate to Twitter
auth = tweepy.OAuthHandler("CQTGkAGL1TSNX5MVShJvXjk7H",
    "nvJopSrix84GSCHShhr4fd0lf4HvZuDvMy0E0b3TQPIlO6LF1L")
auth.set_access_token("794777197470830593-0fQdci4AGivrgv2IQy5CAKW7e1VDf12",
    "kkUxcZC2YGQHuDZpHcvXOiniDW4mXwaTdvQtSjXi7nuax")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
# print("start stream")
#
# (stream.filter(track=["#emoj_flowers"], languages=["en","ar" ]))
#
while True:
        print("start stream")
        try:

            #stream.filter(track=keyword_list, stall_warnings=True)

            stream = tweepy.Stream(api.auth, tweets_listener)
            stream.filter(track=["#emoj_flowers"], languages=["en", "ar"],stall_warnings=True)

        except IncompleteRead as e:
            # Oh well, sleep sometime & reconnect and keep trying again
            time.sleep(15)
            continue
