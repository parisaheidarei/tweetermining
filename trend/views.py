from urllib import request
from geopy import geocoders
from tweepy.models import User
from trend.models import AllUsers, BaseUsers, HashtagTrend, followers
from django.shortcuts import render, HttpResponse
import tweepy as twp
import requests
import json
import datetime
from django.views.generic import ListView
from django.contrib.auth import get_user 
import time
from trend.models import *
#from trend.forms import IndexForm
#from django.views.generic.edit import FormView
from django.http import HttpResponse

from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response
from .filters import HashtagTrendFilter
from .forms import HashtagTrendForm

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

def get_user(thisUser):
    for t in thisUser:
        print(t) 
    return api.get_user(thisUser)

#def BlogView(request):
   # return render(request, 'Home.html')
    
def addUsers(request):   
      
    #Info of users
    baseUsers = BaseUsers.objects.all() 
    for baseUser in baseUsers:
        print(baseUser.userName)
        user =  api.get_user(id =baseUser.userName )

        print("user name is: {}, user location is: {}, user followers count is: {}".format(
        user.name, user.location, user.followers_count))
        #followers = user.followers
        #return HttpResponse(json.dumps(str(followers)))
        #for follower in followers:
            #followerUser = api.get_user(id = follower.user_name)
        #pagenumbers = 0
        #try:
            #pagesNumber = 0
            #if user.followers_count > 500:
              # pagesNumber = user.followers_count // 500
            #if user.followers_count %500 != 0:
               #pagesNumber += 1
            #for page in range(pagesNumber):
            #x = 0
               #for page in twp.Cursor(api.followers, screen_name="twitterDev",wait_on_rate_limit=True, count=10).pages(page):
                #x += 1
                #print('the type of page:', type(page))
                   #followersOfPage = page.screen_name
                   #followersOfPage = page.user_name
                    #if "screen_name" in page:
                       #print(page["screen_name"])
                    #elif "user_name" in page: 
                       #print(page["user_name"])  
                        
        #except twp.TweepError:
            #time.sleep(120)           
                    
        ##x = 0
        #for followerUser in twp.Cursor(api.followers,wait_on_rate_limit=True, screen_name =baseUser.userName).items(user.followers_count): 
            #x += 1
            #followers = followerUser(id)
            #location = followers.location
            #print("The location of the followers is : " + location)
                            
            #def geo(location):
                #g = geocoders.Nominatim(follower_agent='followerUser')
                #if location is not None:
                    #loc = g.geocode(location, timeout=None)
                    #if loc.latitude and loc.longitude is not None:
                        #return loc.latitude, loc.longitude
        followerUser = twp.Cursor(api.followers,wait_on_rate_limit=True, screen_name=baseUser.userName).items(user.followers_count)
        for u in followerUser:     
            userName =u.screen_name
            name =u.name
            location =u.location  
            #print("The location of the followers is : " + location)
            #print("name:"+name,"screen_name:"+screen_name,"location:"+location)
            if 'iran' in location or 'ایران' in location or 'Islamic Republic of Iran' in location or 'تهران' in location or 'جمهوری اسلامی ایران' in location or 'Tehran' in location:
                #print("The location of the followers is : " + location)
                sameUserCount = AllUsers.objects.filter(userName=u.screen_name).count()
                if sameUserCount == 0:
                   AllUsers.objects.create(userName=u.screen_name, name=u.name)
                else:
                    print('user is duplicated')
                #class StdOutListener(StreamListener):
                    #def on_data(self, data):
                      #process stream data here
                      #print(data)
                    #def on_error(self, status):
                      #print(status)
                #if __name__ == '__main__':
                  #listener = StdOutListener()
                  #twitterStream = Stream(auth, listener)
                  #twitterStream.filter(follow=['userName'])  
                  #print('done')                 
                #AllUsers.objects.create(userName=u.screen_name, name=u.name)
            #print(x,followerUser.screen_name, followerUser.followers_count)
            #print('this is follower user location: ', followerUser.location)
            #def status_on(self,status):
                #try:
                    #locations = status.followerUser.location
                    #if 'iran' in locations.followerUser :
                    #Save to database
                        #AllUsers.objects.create(userName=followerUser.screen_name, name=followerUser.name)
                #except:
                    #pass
            #if 'iran' in followerUser or 'ایران' in followerUser or 'Islamic Republic of Iran' in followerUser or 'تهران' in followerUser or 'جمهوری اسلامی ایران' in followerUser or 'Tehran' in followerUser:
                
                #AllUsers.objects.create(userName=followerUser.screen_name, name=followerUser.name)
        #screen_name = []
        #for page in twp.Cursor(api.followers, screen_name="twitterDev", count=10).pages(2):
            #screen_name.extend(page)
            #print(page)
            #time.sleep(60)
            #print (screen_name)
            #print(page)  
            #print("follower name is: {}, follower location is: {}, follower followers count is: {}".format(
            #follower.name, follower.location, follower.followers_count))
        #screen_name = "baseUser"
        #for followerUser in twp.Cursor(api.followers, screen_name="twitterDev").items(30):
            #print(followerUser.screen_name)
         
        #for followerUser in api.followers(screen_name =baseUser.screen_name):
            #print(followerUser.screen_name)
        #def get_followers(screen_name):
            #print('Getting Follower list of ',screen_name)
            #followers = []
            #print(followers)
            #followers_screenNames = []
            #users = twp.Cursor(api.followers, screen_name='@'+screen_name, wait_on_rate_limit=True,count=200)  
#screen_name = "imessi"
#for follower in twp.Cursor(api.followers,screen_name).items(30):
    #user = api.get_user(follower.screen_name)
    #print(follower.screen_name,"Location:" ,user.location)
    return HttpResponse('done')
    #return render(request,'home.html')
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

def get_user(thisUser):
    for t in thisUser:
        print(t) 
    return api.get_user(thisUser)

def getHashtags(request):   
      
    #Info of users
    baseUsers = AllUsers.objects.all() 
    for baseUser in baseUsers:
        try:
        #print(baseUser.userName)
         user =  api.get_user(id =baseUser.userName )
        except twp.error.TweepError:
            pass
        print("user name is: {}, user location is: {}, user followers count is: {}".format(
        user.name, user.location, user.followers_count))
        try:
        #Get tweets of a user
         tweets = api.user_timeline(screen_name= baseUser.userName, count = 1000, include_rts= False, tweet_mode='extended')
        except twp.error.TweepError:
            pass
        for tw in tweets:
            # if tw.created_at > datetime.datetime.now() - datetime.timedelta(days=7):
            allTweetWords = tw.full_text.split(' ')
            for word in allTweetWords:
                if '#' in word:
                    hashtag = HashtagTrend.objects.filter(name=word).count()
                    if hashtag > 0:
                        hashtag = HashtagTrend.objects.get(name=word)
                        twoSecondsAgo =  datetime.datetime.now() - datetime.timedelta(seconds=120)
                       
                        if  baseUser.checked.replace(tzinfo= None) > twoSecondsAgo:
                            hashtag.preRepeat = hashtag.repeat
                            hashtag.repeat = 0
                            hashtag.save()
                            print("user checked now.")

                        hashtag.repeat += 1
                        hashtag.save()                            

                        baseUser.save()

                        print("{} hashtag foun {} time(s).".format(word, hashtag.repeat))


                    else:
                        HashtagTrend.objects.create(
                            name = word,
                            repeat = 1
                        )
                        print("{} hashtag foun as new.".format(word))

        print('all {} tweets checked!'.format(baseUser.name))
    print('all done')
    return HttpResponse('done')
    #return render(request,"home.html")
#def getHashtagsView(request):
    #return render(request,'home.html')
def viewHome(request):
    context = {'HashtagTrend':HashtagTrend.objects.all()}
    return render(request, "home.html", context)    

#def getHashtagsDetail(request,num):
    #return render(request,'index.html')
    #return HttpResponse(num)

def viewIndex(request):
    context = {'HashtagTrend':HashtagTrend.objects.all()}
    return render(request, "index.html", context)    

def viewTrend(request):
    name = "NAME"
    context = {'name': name}
    return render(request, "trend.html", context)      

#def viewChart(request):
    #context = {'HashtagTrend':HashtagTrend.objects.all()}
    #return render(request, "chart.html", context)   
HashtagTrend = get_user_model()

class viewChart(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {})

def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) # http response

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = HashtagTrend.objects.all().count()
        labels = ["HashtagTrend", "#رئیسی#✌️", "خوزستان_را_دریابید#", "گرانی#", "واکسن#", "حسن_روحانی"]
        default_items = [qs_count, 57, 13, 89, 45, 42]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)

def viewTable(request):
    context = {'HashtagTrend':HashtagTrend.objects.all()}
    return render(request, "table.html", context)  

def viewTableSearch(request):
    context = {'HashtagTrend':HashtagTrend.objects.all()}
    return render(request, "table-search.html", context) 

def viewSecondTable(request):
    context = {'HashtagTrend':HashtagTrend.objects.all()}
    return render(request, "secondtable.html", context)     

def viewTableFilter(request):
    hashtag = HashtagTrend.objects.all()
    myFilter = HashtagTrendFilter(request.GET,queryset=hashtag)
    hashtag = myFilter.qs
    context = {'HashtagTrend':hashtag,'myFilter':myFilter}
    return render(request, "table-filter.html", context)  

class viewjsontable(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'jsontable.html', {})    
def get_data(request, *args, **kwargs):
    data = {
        "name": 6,
        "Repeat": 6,
        "createDate": 6,
    }
    return JsonResponse(data) # http response      

class viewjsonresponse(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'jsonresponse.html', {})    
def get_data(request, *args, **kwargs):
    data = {
        "name": 6,
        "Repeat": 6,
        "createDate": 6,
    }
    return JsonResponse(data) # http response   