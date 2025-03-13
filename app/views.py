from django.shortcuts import render

def index(request):
    context = {
        'titile': 'Sempai Anime'
    }
    return render(request, 'app/index.html', context)
