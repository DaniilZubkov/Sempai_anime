from django.shortcuts import render
from animes.models import AnimeTitle, Anime

def index(request):
    anime_titles = Anime.objects.all()[:5]
    new_anime_titles = Anime.objects.all().order_by('-release_date')
    context = {
        'titile': 'Sempai Anime',
        'anime_titles': anime_titles,
        'new_anime_titles': new_anime_titles
    }
    return render(request, 'app/index.html', context)
