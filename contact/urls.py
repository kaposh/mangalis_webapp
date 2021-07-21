from django.urls import path

from . import views

app_name = 'contact'
urlpatterns = [
    # ex: /contact/
    path('', views.contact, name='contact'),
    path('success', views.success, name='success'),
]