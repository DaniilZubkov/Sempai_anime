from django.shortcuts import render

def manga(request):
    context = {
        'title': 'Sempai Anime - Manga',
    }
    return render(request, 'manga/manga.html', context)
