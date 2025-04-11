from django.urls import path, include
from .views import MangaDetailView, CapitelDetailView, TomDetailView, MangaListView

app_name = 'manga'

urlpatterns = [
    path('', MangaListView.as_view(), name='read_manga'),
    path('<slug:manga_slug>/', MangaDetailView.as_view(), name='manga_detail_view'),
    path('<slug:manga_slug>/<slug:tom_slug>/<slug:capitel_slug>/', CapitelDetailView.as_view(), name='capitel_detail'),
    path('<slug:manga_slug>/<slug:tom_slug>', TomDetailView.as_view(), name='tom_detail')
]