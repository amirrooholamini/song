from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

music_items = [
    {"id": 1, "name": "قمیشی", "singer": "ghomayshi"},
    {"id": 2, "name": "شادمهر", "singer": "shadmehr"},
    {"id": 3, "name": "محسن یگانه", "singer": "mohsen yeganeh"},
    {"id": 4, "name": "محسن یگانه", "singer": "mohsen yeganeh"},
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

def standard_music_list(request, name):
    filter_list = []
    for item in music_items:
        if name in item["name"]:
            filter_list.append(item)

    context = {"musics": filter_list}
    return render(request, 'music/list.html', context=context)

def detail(request, id):
    # return HttpResponse(f"music detail of music: {id}")
    selected_music = {}
    for item in music_items:
        if item["id"] == id:
            selected_music = item
            break

    return render(request, "music/detail.html", context=selected_music)

def detail2(request):
    id = request.GET.get("id", 0)
    return HttpResponse(id)