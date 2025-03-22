from django.urls import path
from .views import anime, single_anime_detail

app_name = 'animes'

urlpatterns = [
    path('', anime, name='anime'),
    path('<slug:anime_slug>/', single_anime_detail, name='anime_show'),
    # path('<slug:anime_slug>/<int:episode_numer>/', single_anime_detail, name='anime_episode')
    path('<slug:anime_slug>/<int:page>/', single_anime_detail, name='anime_episode'),
]