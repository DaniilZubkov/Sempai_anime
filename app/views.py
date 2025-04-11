import random
from django.views.generic import CreateView, DetailView, ListView
from django.http import Http404
from django.shortcuts import render, redirect
from animes.models import AnimeTitle, Anime


class IndexView(ListView):
    model = Anime
    template_name = 'app/index.html'
    context_object_name = 'anime_titles'
    queryset = Anime.objects.all()[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titile'] = 'Sempai Anime'
        context['new_anime_titles'] = Anime.objects.all().order_by('-release_date')
        context['random_anime'] = Anime.objects.order_by('?').first()
        return context