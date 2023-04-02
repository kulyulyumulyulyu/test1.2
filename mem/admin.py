from django.contrib import admin

from .models import *

class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'struktura', 'dolzhnost', 'nomer')
    list_display_links = ('id', 'struktura')
    search_fields = ('struktura', 'dolzhnost', 'nomer')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'telephone')
    list_display_links = ('id', 'name', 'telephone')
    search_fields = ('id', 'name', 'telephone')

admin.site.register(About, AboutAdmin)
admin.site.register(Contact, ContactAdmin)