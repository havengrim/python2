
from django.contrib import admin
from django.urls import path, include
from . import views
from authentication import views as auth_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', auth_views.index, name='authentication'), 
    path('', views.index, name='index')
]
