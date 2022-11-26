from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = ["О сайте", "Оформить карту", "Переводы", "Обратная связь", "Войти"]

"""
# Create your views here.

#def index(request): #HttpRequest
#    return HttpResponse("Страница приложения mazebank.")
"""

def index(request):
    basedata = Bank.objects.all()
    return render(request, 'mazebank/index.html', {'basedate': basedata, 'menu' : menu, 'title': 'Главная страница'})

def about(request):
    return render(request, 'mazebank/about.html', {'menu' : menu, 'title': 'О сайте'})






























def categories(request, catid):
    if (request.GET):
        print(request.GET)                                       # http://127.0.0.1:8000/cats/1/?name=Gagarina&type=pop
    if (request.POST):
        print(request.POST)                                      #обычно с формами(логин:пароль)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")

def archive(request, year):
    #if int(year) > 2023:
    #    raise Http404()
    if int(year) > 2050:
        return redirect('home', permanent=False)
    #return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>") # http://127.0.0.1:8000/archive/2022/


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')