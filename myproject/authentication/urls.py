from django.urls import path
from .views import register, user_login
from authentication.views import user_login

app_name = 'authentication'

urlpatterns = [
    path('register/', register, name='register'),
    path('authentication/', user_login, name='authentication'),
]