from urllib import request
from trend.models import BaseUsers, followers
from django.shortcuts import render, HttpResponse
import tweepy as twp
import requests
import json
import datetime
from django.views.generic import ListView
from django.contrib.auth import get_user 
import time
import logging
Consumer_Key = "OvVpZMerNf0pT8gWyC5acXVsc"
Consumer_Secret_Key = "uce8W3hJSIt2VN7PxIvHf5xYxCm51HreXrzcjvr8HCPbL67Dss"
Access_Token = "3291075552-1jdLxBLT88FlMqbM1HgXZfFCr0jo9zx7hAuXPff"
Access_Token_Secret = "6znhXjHRf3t7PknM933Odt0MvkaofTl021pHF4AeTpSxr"

#Authenticate to twitter
auth = twp.OAuthHandler(Consumer_Key,Consumer_Secret_Key)
auth.set_access_token(Access_Token,Access_Token_Secret)
api = twp.API(auth)

try:
    api.verify_credentials()
    print('auth ok')
except:
    print('auth not ok!')



  
def get_followers(api, screen_name, max_connections=0):
    followers = []
    max_connections_reached = False
    try:
        for follower_ids in twp.Cursor(
                api.followers_ids, screen_name=screen_name).pages():
            if max_connections and (
                    len(followers) + len(follower_ids)) > max_connections:
                logging.info(
                    'Max connections reached... trimming final request')
                follower_ids = follower_ids[:max_connections - len(followers)]
                max_connections_reached = True
            followers.extend(api.lookup_users(api, follower_ids))
            if max_connections_reached:
                break
            
    except Exception as e:
        logging.error('Error fetching friends: {}'.format(e))
    return followers
       
    return HttpResponse('done')
    