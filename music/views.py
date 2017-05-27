# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views import generic
from .models import Album
from .models import Song
from .forms import SongForm
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy


# IndexView Class
class IndexView(generic.ListView):
    template_name = "music/index.html"
    # pass data as albums_list
    context_object_name = "all_albums"

    def get_queryset(self):
        return Album.objects.all()


# DetailView Class
class DetailView(generic.DetailView):
    model = Album
    template_name = "music/detail.html"


# django class based form
class AlbumCreate(CreateView):
    model = Album
    template_name ="music/album_form.html"
    fields = ["artist","name","genre","logo"]

    # set the album owner to current user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AlbumCreate, self).form_valid(form)


class AlbumUpdate(UpdateView):
    model = Album
    template_name = "music/album_form.html"
    fields = ["artist", "name", "genre", "logo"]

    # check if the current user owns the album
    def get_queryset(self):
        base_qs = super(AlbumUpdate, self).get_queryset()
        return base_qs.filter(user=self.request.user)


class AlbumDelete(DeleteView):
    model = Album
    # redirect to this url after deletion
    success_url = reverse_lazy('music:index')


# django class based form
class SongCreate(CreateView):

    template_name ="music/song_form.html"
    form_class = SongForm

    def get_form_kwargs(self):
        kwargs = super(SongCreate, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

def updateProfilePic(request):
    pass








