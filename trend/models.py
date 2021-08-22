from django.db import models


class BaseUsers(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    userName = models.CharField(max_length=250)
    checked = models.BooleanField(default=False)
    createDate = models.DateTimeField(auto_now_add=True)
  
    
    def __str__(self):
        return self.userName


class AllUsers(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    userName = models.CharField(max_length=250)
    createDate = models.DateTimeField(auto_now_add=True)
    checked = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.userName

class HashtagTrend(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250,null=True)
    repeat = models.IntegerField(default=0)
    preRepeat = models.IntegerField(default=0)
    createDate = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        #return self.name
        return "{}-{}-{}-{}-{}".format(self.id,self.name,self.reapet,self.prerepeat,self.createdate)

def followers(self, **kargs): 
    return self._api.followers(user_id=self.id, **kargs) 



