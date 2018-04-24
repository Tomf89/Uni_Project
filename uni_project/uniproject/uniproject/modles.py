from django.db import models
from django.contrib.auth.models import User

from mongoengine import *

connect("auth_user")

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following_artists = models.TextField(max_length=500, blank=True)