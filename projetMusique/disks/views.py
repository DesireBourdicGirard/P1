from django.shortcuts import render
from .models import Album, Track

def accueil(request):
    """Afficher tous les albums de notre liste"""
    albums = Album.objects.all()
    return render(request, 'disks/accueil.html', {'albums':albums})

def lire(request, album_id):
    """Afficher un album"""
    tracks = Track.objects.filter(album=album_id)
    return render(request, 'disks/lire_album.html', locals())