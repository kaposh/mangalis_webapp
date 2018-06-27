from django.views import generic
from .models import Souvenir

class IndexView(generic.ListView):
    template_name = 'catalog/index.html'
    context_object_name = 'available_souvenirs'
    def get_queryset(self):
        """Returns active souvenirs"""
        return Souvenir.objects.filter(
            available=True
        ).order_by('name')