
from django.contrib import admin

from .models import Souvenir,Kategoria

admin.site.register(Kategoria)

@admin.register(Souvenir)
class SouvenirAdmin(admin.ModelAdmin):
  list_display = ('name', 'code', 'kategoria', 'available')
  search_fields = ['name', 'code']
  list_filter = ('kategoria',)
