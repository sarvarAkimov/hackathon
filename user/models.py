from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import settings
from django_quill.fields import QuillField
# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=450, default='Akimov Sarvar')
    photo = models.ImageField(upload_to='media', blank='True')
    password = models.CharField(max_length=150)
    id = models.AutoField(unique=True, primary_key=True)

    credit_card = models.BigIntegerField(blank=True, null=False, default=1235123112341234)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Xamshira(models.Model):
    id = models.AutoField(unique=True,primary_key=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True)
    shifoxona = models.ForeignKey('Hospitals',on_delete=models.CASCADE,related_name='hospital')
    kasb = models.ForeignKey('Occupation',on_delete=models.CASCADE,related_name='occupations')
    passport = models.FileField(upload_to='pasports', blank=True, null=True)
    minut_10 = models.BigIntegerField()
    minut_20 = models.BigIntegerField()
    paid = models.BooleanField(default=False)

class Hospitals(models.Model):
    id = models.AutoField(unique=True,primary_key=True)
    name = models.CharField(max_length=250)
    longitud = models.CharField(max_length=150)
    latitud = models.CharField(max_length=150)
    main_nurse = models.OneToOneField('Xamshira', on_delete=models.DO_NOTHING, null=True, blank=True)
    tez_yordam = models.ManyToManyField('Xamshira', related_name='ambulance', blank=True)
    credit_card = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class Occupation(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Post_maqolas(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=150)
    photos = models.ImageField(upload_to='media')
    quil = QuillField()
    author = models.ForeignKey(Xamshira, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    liked = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

class Post_tabletkas(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='media')
    quil = QuillField()
    kasalik = models.ManyToManyField('Kassallik')
    liked = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    def __str__(self):
        return self.name

class Kassallik(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name