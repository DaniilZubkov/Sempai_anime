from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .models import AnimeTitle, Anime
from django.views.generic import DetailView
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.http import JsonResponse

import random
from django.core.cache import cache

def anime(request):
    anime_titles = Anime.objects.all()
    anime2 = AnimeTitle.objects.order_by('episode_numer').first()

    context = {
        'titile': 'Sempai Anime',
        'anime_titles': anime_titles
    }
    return render(request, 'animes/anime.html', context)


def single_anime_detail(request, anime_slug, page=1):
    anime = get_object_or_404(Anime, slug=anime_slug)
    episodes = anime.episodes.all()

    paginator = Paginator(episodes, 1) # 10 серий на страницу
    current_page = paginator.page(page)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

    context = {
        'titile': 'Sempai Anime',
        'anime': anime,
        'episodes': current_page,
        'slug_url': anime_slug
    }

    return render(request, 'animes/single_anime_title.html', context)



def random_anime(request):
    random_anime = cache.get('random_anime')
    if not random_anime:
        random_anime = Anime.objects.order_by('?').first()
        cache.set('random_anime', random_anime, 300)  # Кэш на 5 минут
    return {'random_anime': random_anime}