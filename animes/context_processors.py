from animes.models import Anime
import random

def random_anime(request):
    return {
        'random_anime': Anime.objects.order_by('?').first()
    }