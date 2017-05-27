# modules required to be imported for the creation of the form
from django.contrib.auth.models import User
from django import forms
from .models import Song
from .models import Album


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ["name", "album", "file_type"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(SongForm, self).__init__(*args, **kwargs)
        self.fields['album'].queryset = Album.objects.filter(user=user)








