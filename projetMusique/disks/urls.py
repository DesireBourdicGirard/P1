from django.urls import path
from . import views

urlpatterns = [

    path('accueil/', views.accueil, name='accueil'),
    path('album/<int:album_id>', views.lire, name='lire_album')

]
