from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tweet(models.Model):
    body = models.TextField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    likes = models.ManyToManyField(User, related_name='likes')


class HashTag(models.Model):
    name = models.CharField(max_length=64, unique=True)
    post = models.ManyToManyField(Tweet)
    count = models.IntegerField(default=0)

