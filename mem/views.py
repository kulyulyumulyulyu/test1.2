from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .forms import ContactForm
from .models import *

menu = [
    {'title': "О нас", 'url_name': 'ab'},
    {'title': "Найти сотрудника", 'url_name': 'find'},
    {'title': "Обрантная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'}
]

def index(request):
    posts = About.objects.all()
    context = {
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'mem/index.html', context=context)

def ab(request):
    return render(request, 'mem/ab.html', {'menu': menu, 'title': 'О нас'})

def find(request):
    return render(request, 'mem/find.html', {'menu': menu, 'title': 'Найти сотрудника'})

def contact(request):
    form = ContactForm()
    context = {
        'form': form,
        'menu': menu,
        'title': 'Обратная связь'
    }
    return render(request, 'mem/contact.html', context)

def login(request):
    return render(request, 'mem/login.html', {'menu': menu, 'title': 'Авторизация'})

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')