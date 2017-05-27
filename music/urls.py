from django.conf.urls import url,include
from django.contrib.auth.decorators import login_required
from . import views

app_name = "music"
urlpatterns = [
    url(r'^$',views.IndexView.as_view(), name = "index"),
    url(r'^(?P<pk>\d+)$',views.DetailView.as_view(), name = "detail"),
    url(r'^album/add/$',login_required(views.AlbumCreate.as_view()), name="album-create"),
    url(r'^album/(?P<pk>\d+)/update/$',login_required(views.AlbumUpdate.as_view()), name='album-update'),
    url(r'^album/(?P<pk>\d+)/delete/$',login_required(views.AlbumDelete.as_view()), name='album-delete'),
    url(r'^song/add/$', login_required(views.SongCreate.as_view()), name="song-create"),
    #user registraion path
]