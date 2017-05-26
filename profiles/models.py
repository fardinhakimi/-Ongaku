# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# User Profile Model
# extending the user model

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True, auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=20, blank=True, default="")
    profile_picture = models.FileField(max_length=255)

    def __str__(self):
        return self.user.username
# get or create a user profile, useful for profile update
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

