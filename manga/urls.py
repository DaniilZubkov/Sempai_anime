from django.urls import path, include
from .views import manga

app_name = 'manga'

urlpatterns = [
    path('', manga, name='read_manga'),
    # path('upload/', CreatePostView.as_view(), name='upload_manga')
]