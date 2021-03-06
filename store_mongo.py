#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
4 December 2017
.. codeauthor: svitlana vakulenko
    <svitlana.vakulenko@gmail.com>

'''

from twython import TwythonStreamer

from pymongo import MongoClient

from twitter_settings import *


def connect_to_mongo(db, collection):
    client = MongoClient('localhost', 27017)
    return client[db][collection]


collection = connect_to_mongo("tweets", "sample_04_12_2017")


class MyStreamer(TwythonStreamer):

    def on_success(self, data):
        if 'text' in data:
            print(data['text'])
            collection.insert_one(data)
            print collection.count()

    def on_error(self, status_code, data):
        print(status_code)



stream = MyStreamer(APP_KEY, APP_SECRET,
                    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
stream.statuses.sample()
