from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os
from django.views.generic import CreateView, DetailView
from .models import Manga, Capitel, Tom



def manga(request):
    manga_list = Manga.objects.all()
    context = {
        'titile': 'Sempai Anime',
        'manga_list': manga_list,
    }
    return render(request, 'manga/manga.html', context)


class MangaDetailView(DetailView):
    model = Manga
    template_name = 'manga/manga_detail.html'
    slug_url_kwarg = 'manga_slug'
    context_object_name = 'manga'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Получаем все тома с предзагруженными главами
        toms = self.object.toms.all().prefetch_related('capitels')

        # Собираем все главы из всех томов
        all_capitels = []
        for tom in toms:
            all_capitels.extend(tom.capitels.all())

        context['all_capitels'] = all_capitels
        context['toms'] = toms
        return context



class TomDetailView(DetailView):
    model = Tom
    template_name = 'manga/tom_detail.html'
    slug_url_kwarg = 'tom_slug'
    context_object_name = 'tom'

    def get_queryset(self):
        return super().get_queryset().select_related('manga')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'manga': self.object.manga,
            'capitels': self.object.capitels.order_by('captel_number')
        })
        return context





class CapitelDetailView(DetailView):
    model = Capitel
    template_name = 'manga/capitel_detail.html'
    slug_url_kwarg = 'capitel_slug'
    context_object_name = 'capitel'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pages'] = self.object.pages.all().order_by('page_number')

        # Получаем все главы манги
        all_capitels = self.object.manga_set.first().capitel_set.all()

        current_index = list(all_capitels).index(self.object)

        context['pages'] = self.object.pages.all().order_by('page_number')
        context['previous_chapter'] = all_capitels[current_index - 1] if current_index > 0 else None
        context['next_chapter'] = all_capitels[current_index + 1] if current_index < len(all_capitels) - 1 else None
        return context

