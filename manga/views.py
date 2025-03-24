from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os
from django.views.generic import CreateView
from .models import Manga



def manga(request):
    manga_list = Manga.objects.all()
    context = {
        'titile': 'Sempai Anime',
        'manga_list': manga_list,
    }
    return render(request, 'manga/manga.html', context)




