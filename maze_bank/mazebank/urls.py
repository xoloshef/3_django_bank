from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('index', index, name='home'),
    path('index.html', index, name='home'),
    path('more/index.html', index, name='home'),
    path('about/', about, name='about'),
    path('more/login.html/', login, name='login'),
    path('more/register.html/', register, name='register'),
    path('about/', about, name='about'),
    path('about/', about, name='about'),
    path('about/', about, name='about'),

    path('cats/<int:catid>/', categories),
    re_path(r'archive/(?P<year>[0-9]{4})/', archive)
]
