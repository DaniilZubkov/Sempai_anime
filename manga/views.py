from django.shortcuts import render, get_object_or_404
from django.core.files.storage import FileSystemStorage
import os
from django.views.generic import CreateView, DetailView
from django.core.paginator import Paginator
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

    def get_object(self, queryset=None):
        # Получаем том по связям manga_slug + tom_slug
        return get_object_or_404(
            Tom,
            slug=self.kwargs['tom_slug'],
            manga__slug=self.kwargs['manga_slug']
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'manga': self.object.manga,  # автоматически доступно через ForeignKey
            'capitels': self.object.capitels.all().order_by('captel_number')
        })
        return context





class CapitelDetailView(DetailView):
    model = Capitel
    template_name = 'manga/capitel_detail.html'
    slug_url_kwarg = 'capitel_slug'
    context_object_name = 'capitel'

    paginate_by = 1

    def get_object(self, queryset=None):
        return get_object_or_404(
            Capitel,
            slug=self.kwargs['capitel_slug'],
            tom__slug=self.kwargs['tom_slug'],
            tom__manga__slug=self.kwargs['manga_slug']
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['pages'] = self.object.pages.all().order_by('page_number')
        page_list = self.object.pages.all().order_by('page_number')
        paginator = Paginator(page_list, self.paginate_by)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context.update({
            'manga': self.object.tom.manga,
            'tom': self.object.tom,
            'page_obj': page_obj,

            'paginator': paginator,
            'is_paginated': page_obj.has_other_pages()
        })
        return context

    def get_queryset(self):
        return super().get_queryset().prefetch_related('pages')
