from django.db import models

# Create your models here.

class userdata(models.Model):
    username = models.CharField(max_length=10,primary_key=True,unique=True)
    name = models.CharField(max_length=225)
    phoneno = models.BigIntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=8)
    createddate = models.DateField(auto_now=True)