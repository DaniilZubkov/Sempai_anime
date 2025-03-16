from django.shortcuts import render
from animes.models import AnimeTitle, Anime

def index(request):
    anime_titles = Anime.objects.all()[:5]
    context = {
        'titile': 'Sempai Anime',
        'anime_titles': anime_titles,
    }
    return render(request, 'app/index.html', context)
