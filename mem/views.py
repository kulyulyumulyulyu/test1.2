from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import ContactForm
from .models import *
from .utils import *


def index(request):
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
    error = ''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была не верной'

    form = ContactForm()
    contex = {
        'form': form,
        'menu': menu,
        'error': error,
        'title': 'Обратная связь'
    }
    return render(request, 'mem/contact.html', contex)


# def login(request):
# return render(request, 'mem/login.html', {'menu': menu, 'title': 'Авторизация'})

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'mem/login.html'

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')
