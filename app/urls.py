from .views import IndexView
from django.urls import path

app_name = 'app'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # This maps the root URL to the index view.
]