from django.views import generic
from django.shortcuts import get_object_or_404, render
from .models import Souvenir, Kategoria

def product_list(request, category_slug=None):
    category=None
    categories=Kategoria.objects.all()
    souvenirs = Souvenir.objects.filter(available=True)
    if category_slug:
        category=get_object_or_404(Kategoria, slug=category_slug)
        souvenirs=souvenirs.filter(kategoria=category)
    return render(request,'catalog/index.html', {'category': category,
                                                  'categories':categories,
                                                  'souvenirs':souvenirs})

def product_detail(request, product_slug, id):
    souvenir =get_object_or_404(Souvenir, id=id, slug=product_slug, available=True)
    return render(request,'catalog/detail.html', {'suvenir':souvenir})
