from django.urls import path

from . import views

app_name = 'contact'
urlpatterns = [
    # ex: /catalog/
    path('', views.contact, name='contact'),
]