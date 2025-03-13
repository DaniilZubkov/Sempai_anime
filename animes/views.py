from django.shortcuts import render, get_object_or_404, redirect
from .models import AnimeTitle, Anime
from django.views.generic import DetailView


def anime(request):
    anime_titles = Anime.objects.all()
    anime2 = AnimeTitle.objects.order_by('episode_numer').first()

    context = {
        'titile': 'Sempai Anime',
        'anime_titles': anime_titles
    }
    return render(request, 'animes/anime.html', context)


def single_anime_detail(request, anime_slug):
    # anime = Anime.objects.get(slug=anime_slug)
    # anime_titles = anime.objects.get()
    # context = {
    #     'titile': 'Sempai Anime',
    #     'anime': anime,
    #     'anime_titles': anime_titles
    # }
    # return render(request, 'animes/single_anime_title.html', context)

    anime = get_object_or_404(Anime, slug=anime_slug)
    episodes = anime.episodes.all()
    context = {
        'titile': 'Sempai Anime',
        'anime': anime,
        'episodes': episodes
    }
    return render(request, 'animes/single_anime_title.html', context)