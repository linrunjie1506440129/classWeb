from django.db import models
from django.contrib.auth.models import User

class ClassNews(models.Model):
    ntitle = models.CharField(max_length=30)
    ntext = models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text

class ClassNote(models.Model):
    otitle = models.CharField(max_length=30)
    otext = models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text

class ClassActive(models.Model):
    atitle = models.CharField(max_length=30)
    atext = models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text

class MessageBox(models.Model):
    name = models.CharField(max_length=8)
    text = models.TextField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(u"姓名",max_length=32)
    def __unicode__(self):
       return self.name

