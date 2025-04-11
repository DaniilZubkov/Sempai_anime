from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .models import AnimeTitle, Anime
from django.views.generic import DetailView, ListView
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.http import JsonResponse

import random
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator



class AnimeList(ListView):
    model = Anime
    template_name = 'animes/anime.html'
    context_object_name = 'anime_titiles'
    queryset = Anime.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titile'] = 'Sempai Anime'
        return context



class SingleAnimeDetail(DetailView):
    """
        Представление для отображения отдельного эпизода аниме с навигацией между сериями.
        Поддерживает два варианта URL:
        1. По slug: /anime-slug/episode-slug/
        2. По номеру эпизода: /anime-slug/episode-number/
        """
    model = AnimeTitle
    template_name = 'animes/single_anime_title.html'
    context_object_name = 'episode'
    slug_url_kwarg = 'episode_slug'  # имя параметра slug в URL

    def get_object(self, queryset=None):
        """
        Получаем объект эпизода на основе переданных параметров URL.
        Поддерживает поиск по slug или по номеру эпизода.
        """
        anime_slug = self.kwargs.get('anime_slug')
        episode_slug = self.kwargs.get('episode_slug')
        episode_pk = self.kwargs.get('pk')

        # Получаем аниме по slug
        anime = get_object_or_404(Anime, slug=anime_slug)

        if episode_slug:
            # Если передан slug эпизода
            return get_object_or_404(
                AnimeTitle,
                anime=anime,
                slug=episode_slug
            )
        elif episode_pk:
            # Если передан номер эпизода
            return get_object_or_404(
                AnimeTitle,
                anime=anime,
                episode_numer=episode_pk
            )
        else:
            # Если ничего не передано, возвращаем первый эпизод
            return get_object_or_404(
                AnimeTitle,
                anime=anime,
                episode_numer=1
            )

    def get_context_data(self, **kwargs):
        """
        Добавляем в контекст данные для навигации между эпизодами.
        """
        context = super().get_context_data(**kwargs)
        current_episode = self.object

        # Получаем все эпизоды этого аниме, отсортированные по номеру
        all_episodes = AnimeTitle.objects.filter(
            anime=current_episode.anime
        ).order_by('episode_numer')

        # Получаем общее количество эпизодов
        total_episodes = all_episodes.count()

        # Получаем текущую позицию эпизода (для отображения "Эпизод 3 из 12")
        current_position = list(all_episodes.values_list('id', flat=True)).index(current_episode.id) + 1

        # Получаем предыдущий и следующий эпизоды
        previous_episode = all_episodes.filter(
            episode_numer__lt=current_episode.episode_numer
        ).order_by('-episode_numer').first()

        next_episode = all_episodes.filter(
            episode_numer__gt=current_episode.episode_numer
        ).order_by('episode_numer').first()

        # Добавляем дополнительные данные в контекст шаблона
        context.update({
            'titile': 'Sempai Anime',
            'anime': current_episode.anime,  # родительское аниме
            'total_episodes': total_episodes,
            'current_position': current_position,
            'previous_episode': previous_episode,
            'next_episode': next_episode,
            'all_episodes': all_episodes,  # список всех эпизодов
            'episode_range': range(1, total_episodes + 1),  # диапазон номеров для быстрого доступа
        })

        return context



# def random_anime(request):
#     random_anime = cache.get('random_anime')
#     if not random_anime:
#         random_anime = Anime.objects.order_by('?').first()
#         cache.set('random_anime', random_anime, 300)  # Кэш на 5 минут
#     return {'random_anime': random_anime}



class RandomAnimeView(DetailView):
    model = Anime
    template_name = 'animes/single_anime_title.html'

    @method_decorator(cache_page(300))  # Кэшируем всю страницу на 5 минут
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['random_anime'] = Anime.objects.order_by('?').first()
        return context