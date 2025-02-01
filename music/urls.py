from django.urls import path
from . import views

urlpatterns = [
    path('hello', views.hello),
    path('list', views.musics, name='music-list'),
    path('standard-list', views.standard_music_list, name='standard-music-list'),
    path('detail/<id>', views.detail, name='music-detail'),
    
]
