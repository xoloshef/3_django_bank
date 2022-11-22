from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request): #HttpRequest
    return HttpResponse("Страница приложения mazebank.")

def categories(request):
    return HttpResponse("<h1>Статьи по категориям</h1>")