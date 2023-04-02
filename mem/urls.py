from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name = 'home'),
    path('ab/', ab, name ='ab'),
    path('find/', find, name ='find'),
    path('contact/', contact, name ='contact'),
    path('login/', login, name ='login')
]