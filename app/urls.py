from .views import index
from django.urls import path

app_name = 'app'

urlpatterns = [
    path('', index, name='index'), # This maps the root URL to the index view.
]