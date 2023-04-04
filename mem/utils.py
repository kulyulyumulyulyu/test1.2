from .models import *

menu = [
    {'title': "О нас", 'url_name': 'ab'},
    {'title': "Найти сотрудника", 'url_name': 'find'},
    {'title': "Обрантная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'}
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        contact = Contact.objects.all()
        context['menu'] = menu
        context['contact'] = contact
        if 'contact_selected' not in context:
            context['contact_selected'] = 0
        return context