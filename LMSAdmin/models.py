from operator import mod
from turtle import mode
from django.db import models

# Create your models here.
class User(models.Model):
    Id=models.AutoField(primary_key=True)
    Username=models.CharField(max_length=100)
    email=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=20)
    conformpassword=models.CharField(max_length=20)


class Book(models.Model):
    Id=models.AutoField(primary_key=True)
    Bookname=models.CharField(max_length=100)
    Author=models.CharField(max_length=100)
    Noofbooks=models.IntegerField()
    Branch=models.CharField(max_length=100,null=True)

