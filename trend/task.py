# Create your tasks here
from __future__ import absolute_import,unicode_literals
from .import bin
from trend.app import celery
import time
from binance.exceptions import *
from . import Encryption
from celery import shared_task
import time
from django.http import JsonResponse
from .models import HashtagTrend, User
from django.core.serializers import serialize
import json
#app = Celery('tasks', broker='amqp://guest@localhost//')
@shared_task
def update_balance():
    all_hashtagtrend_List = (HashtagTrend.objects.all())
    with open("D:\\twitterproject\\tweeterMining\\tweeterMining\\data.json","w")as f:
        jsoned = json.loads(serialize)
        json.dump(jsoned,f)
        