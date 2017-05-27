# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.

class Album(models.Model):
    # a user can have many albums
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = "")
    artist = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    logo = models.FileField()
    # returns the id of the newly created album

    def get_absolute_url(self):
        return reverse("music:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name

class Song(models.Model):

    File_Type_CHOICES = (

        ('mp3', 'mp3'),
        ('wav', 'wav'),
    )

    # on deletion of the album deletes the child songs
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=20, default= "----", choices=File_Type_CHOICES)
    name = models.CharField(max_length=255)
    is_favorite = models.BooleanField(default=False)

     # redirect to the album detail page
    def get_absolute_url(self):
        return reverse("music:detail", kwargs={"pk": self.album.pk})

    def __str__(self):
        return self.name







