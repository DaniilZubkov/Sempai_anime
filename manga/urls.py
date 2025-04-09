from django.urls import path, include
from .views import manga, MangaDetailView, CapitelDetailView, TomDetailView, MangaListView

app_name = 'manga'

urlpatterns = [
    # path('', manga, name='read_manga'),
    path('', MangaListView.as_view(), name='read_manga'),
    path('<slug:manga_slug>/', MangaDetailView.as_view(), name='manga_detail_view'),
    path('<slug:manga_slug>/<slug:tom_slug>/<slug:capitel_slug>/', CapitelDetailView.as_view(), name='capitel_detail'),
    path('<slug:manga_slug>/<slug:tom_slug>', TomDetailView.as_view(), name='tom_detail')
    # path('upload/', CreatePostView.as_view(), name='upload_manga')
]