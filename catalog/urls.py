from django.urls import path

from . import views

app_name = 'catalog'
urlpatterns = [
    # ex: /catalog/
    path('', views.IndexView.as_view(), name='catalog-index'),
]