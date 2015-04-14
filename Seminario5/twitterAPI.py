#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Julian'
import twitter
import io
import json

#Funcion para la conexion
def oauth_login():
    CONSUMER_KEY = 'JB27DPdy9VyN5PSfkqjBTsZ95'
    CONSUMER_SECRET = 'wWjlvyayPbxvjSrTsoDtnVubXUzh1EAzXBKXtoqnfQIXHFZNHw'
    OAUTH_TOKEN = '3154107761-HLjCHwgmZlPoWeRl5WRhx5ibKBWyVGA0vT2h1zc'
    OAUTH_TOKEN_SECRET = '9UH75YL1soLx7NNbA74J87JYi6Kfwu8vcosO02RRAZrVr'
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    return twitter_api

#Funcion para grabar la informacion en formato JSON
def save_json(filename, data):
    with io.open('{0}.json'.format(filename),'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(data, ensure_ascii=False)))

#Funcion para leer el fichero JSON
def load_json(filename):
    with io.open('{0}.json'.format(filename),encoding='utf-8') as f:
        return f.read()