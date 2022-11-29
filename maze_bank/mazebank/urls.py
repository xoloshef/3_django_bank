from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('index', index, name='home'),
    path('index.html', index, name='home'),
    path('login/index', index, name='home'),
    path('about/', about, name='about'),
    path('login/', login, name='login'),
    path('login.html', login, name='login'),
    path('register/', register, name='register'),
    path('register.html/', register, name='register'),
    path('dontpassword', dontpassword, name='dontpassword'),
    path('login/dontpassword.html/', dontpassword, name='dontpassword'),

    path('client_index/', client_index, name='client_index'),





    path('about/', about, name='about'),
    path('about/', about, name='about'),
    path('about/', about, name='about'),

    path('cats/<int:catid>/', categories),
    re_path(r'archive/(?P<year>[0-9]{4})/', archive)
]
