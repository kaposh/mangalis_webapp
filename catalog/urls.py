from django.urls import path

from . import views

app_name = 'catalog'
urlpatterns = [
    # ex: /catalog/
    path('', views.product_list, name='catalog-index'),
    # ex: /catalog/Odznak/
    path('<slug:category_slug>/', views.product_list, name='catalog-kategoria'),
    # ex: /catalog/Odznak/
    path('<slug:product_slug>/<int:id>', views.product_detail, name='catalog-detail'),
]