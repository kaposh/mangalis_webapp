
from django.contrib import admin

from .models import Souvenir,Kategoria

@admin.register(Kategoria)
class SouvenirAdmin(admin.ModelAdmin):
  list_display = ('name', 'description')
  prepopulated_fields = {'slug':['name',]}


@admin.register(Souvenir)
class SouvenirAdmin(admin.ModelAdmin):
  list_display = ('name', 'code', 'kategoria', 'available')
  search_fields = ['name', 'code']
  list_filter = ('kategoria',)
  prepopulated_fields = {'slug':['name',]}
