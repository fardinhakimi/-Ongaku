# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from .models import Album
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

# IndexView Class
class IndexView(generic.ListView):

    template_name = "music/index.html"
    # pass data as albums_list
    context_object_name = "all_albums"

    def get_queryset(self):
        return Album.objects.all()

#DetailView Class
class DetailView(generic.DeleteView):

    model = Album
    template_name = "music/detail.html"

# django class based form
class AlbumCreate(CreateView):

    model = Album
    template_name ="music/album_form.html"
    fields = ["artist","name","genre","logo"]
class AlbumUpdate(UpdateView):

    model = Album
    template_name = "music/album_form.html"
    fields = ["artist", "name", "genre", "logo"]

class AlbumDelete(DeleteView):
    model = Album
    # redirect to this url after deletion
    success_url = reverse_lazy('music:index')








