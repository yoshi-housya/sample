# coding: utf-8 

from requests_oauthlib import OAuth1Session
import json
import os
import random
import datetime

CK = "LoqNpuBFwxPMS9SLuhgrm1ino"
CS = "ijYm0cE3e8oAcauQtFJ4ey1Ew7Tk4zzxnO9KBQodKiopKdKO1u"
AT = "1022470594766360576-2ukqSvK3pePTSyeAAmNSdnt5swHUmC"
AS = "qMlJmvWWZMKT5DiUkx5avNJplcn0Px8HMHJIXcOSMYWSs"

twitter = OAuth1Session(os.environ[CK],  os.environ[CS], os.environ["AT"], os.environ[AS])

tweets = ["hello,world!!","good night!","good morning"]

randomtweet = tweets[random.randrange(len(tweets))]

timestamp = datetime.datetime.today() + datetime.timedelta(hours=9)
timestamp = str(timestamp.strftime("%Y/%m/%d %H:%M"))

params = {"status": randomtweet + " " + timestamp}
req = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params = params)
