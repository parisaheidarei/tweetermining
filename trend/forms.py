from trend.models import HashtagTrend
from django import forms
from django.shortcuts import render

from django.forms import ModelForm
from .models import AllUsers, HashtagTrend

def index(request):
    try:
        hashtag = HashtagTrend.objects.filter(name='#covid19').count()
        if hashtag > 0:
            hashtag += 1
            print("name".format(hashtag))
            return render (request, 'index.html',)
    except RuntimeError:
        pass



class HashtagTrendForm(ModelForm):
    class Meta :
        model = HashtagTrend
        fields = '__all__'

class AllUsersForm(ModelForm):
    class Meta :
        model = AllUsers
        fields = '__all__'        