from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

music_items = [
    {"id": 1, "name": "song_1", "singer": "ghomayshi"},
    {"id": 2, "name": "song_2", "singer": "shadmehr"},
    {"id": 3, "name": "song_3", "singer": "mohsen yeganeh"},
]


def hello(request):
    return HttpResponse("Done!")

def musics(request):
    data = ""
    for item in music_items:
        data = data + f"id: {item['id']} , name: {item['name']} , singer: {item['singer']}" + "<br>"
    return HttpResponse(data)

def detail(request):
    return HttpResponse("music detail")

