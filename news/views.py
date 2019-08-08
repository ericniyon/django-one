from django.views import generic
from django.views.generic.edit import CreateView
from django.shortcuts import render, get_object_or_404
from .models import Album, Song
# desplay the album with status 1 on my home page
def AlbumView(request):
    album = Album.objects.filter(status=1)
    context={
        'albums':album
    }
    template = 'album.html'
    return render(request, template, context)


#album detail views
def AlbumDetails(request, id):
    album_d = get_object_or_404(Album, pk=id)
    context = {
        'album_d':album_d
    }
    template = 'album_details.html'
    return render(request, template, context)

def AdminDashbord(request):
    template = 'index.html'
    return render(request,template)
def MyDaashoard(request):
    template = 'dashboard.html'
    return render(request,template)
#adding new album into my model
class ToaddAlbum(generic.CreateView):
    model = Album
    fields = ['title','artist','album_logo']
    template_name = 'album_form.html'
#adding song to album functin
class AddSongToAlbum(generic.CreateView):
    model = Song
    fields = ['name','song_type','song_formt','album']
    template_name = 'song_form.html'


