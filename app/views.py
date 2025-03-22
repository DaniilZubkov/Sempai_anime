import random

from django.http import Http404
from django.shortcuts import render, redirect
from animes.models import AnimeTitle, Anime

def index(request):
    anime_titles = Anime.objects.all()[:5]
    new_anime_titles = Anime.objects.all().order_by('-release_date')
    random_anime = Anime.objects.order_by('?').first()

    context = {
        'titile': 'Sempai Anime',
        'anime_titles': anime_titles,
        'new_anime_titles': new_anime_titles,
        'random_anime': random_anime,
    }
    return render(request, 'app/index.html', context)
