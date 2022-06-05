from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.conf import settings
from user.models import Xamshira,User


class Check_time(models.Model):
    id = models.AutoField(unique=True,primary_key=True)
    vaqt = models.ForeignKey('Time',related_name='time',on_delete=models.CASCADE,blank=True)
    user = models.ForeignKey(Xamshira,related_name='time',on_delete=models.CASCADE,blank=True)
    date = models.DateField()
    from_user_check = models.ForeignKey(User,on_delete=models.CASCADE,related_name='check_from',null=True)

class Chat(models.Model):
    id = models.AutoField(unique=True,primary_key=True)
    messages = models.ManyToManyField('Messages',related_name='all_messages')
    from_user = models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True,related_name='chat_from_users')
    to_users = models.ManyToManyField(Xamshira,related_name='xamshiras')
    savol = models.TextField()
    is_closed = models.BooleanField(default=False)

    def __str__(self):
        return self.savol

class Messages(models.Model):
    id = models.AutoField(unique=True,primary_key=True)
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.DO_NOTHING,null=True,blank=True,related_name='from_users')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name='likes')
    def __str__(self):
        return self.text




class Time(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Notification(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)
    xamshira = models.OneToOneField(Xamshira,on_delete=models.DO_NOTHING,related_name='del_xamshira',null=True,blank=True)
    chat = models.OneToOneField('Chat',on_delete=models.CASCADE,related_name='nft_chat',null=True,blank=True)
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='nft_to')

class Transactions(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    from_card = models.BigIntegerField()
    to_card = models.BigIntegerField()
    summ = models.BigIntegerField()
    to_us = models.BigIntegerField()
    from_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='money_from')




