from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

music_items = [
    {"id": 1, "name": "قمیشی", "singer": "ghomayshi"},
    {"id": 2, "name": "شادمهر", "singer": "shadmehr"},
    {"id": 3, "name": "محسن یگانه", "singer": "mohsen yeganeh"},
]


def hello(request):
    url = reverse('music-list')
    return HttpResponseRedirect(url)

def musics(request):
    data = ""
    for item in music_items:
        url = reverse('music-detail', args=[item['id']])
        data = data + f"<a href='{url}' target='_blank'>{item['name']}</a>" + "<br>"
    return HttpResponse(data)

def standard_music_list(request):
    return render(request, 'music/list.html')

def detail(request, id):
    return HttpResponse(f"music detail of music: {id}")

