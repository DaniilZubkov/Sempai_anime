from django.urls import path
from .views import SingleAnimeDetail, AnimeList

app_name = 'animes'

urlpatterns = [
    path('', AnimeList.as_view(), name='anime'),
    path('<slug:anime_slug>/', SingleAnimeDetail.as_view(), name='anime_show'),  # для главной страницы аниме
    path('<slug:anime_slug>/<slug:episode_slug>/', SingleAnimeDetail.as_view(), name='anime_episode'),  # по slug эпизода
    path('<slug:anime_slug>/<int:pk>/', SingleAnimeDetail.as_view(), name='anime_episode_by_number'),  # по номеру эпизода
]