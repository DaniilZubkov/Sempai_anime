from django.urls import path
from .views import UserLoginView, UserProfileView, UserRegistrationView, logout


app_name = 'users'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('register/', UserRegistrationView.as_view(), name='user_register'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('logout/', logout, name='user_logout'),
]