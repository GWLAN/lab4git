#-*-coding:utf-8-*-
from django.db import models
from django.contrib import admin
# Create your models here.
class Author(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.CharField(max_length=100,blank = True)
