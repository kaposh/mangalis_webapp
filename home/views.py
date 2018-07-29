from django.shortcuts import render
from contact.models import Firma
from django.views import generic
# Create your views here.
def index(request):
    """
    View function for home page of site.
    """
    mangalis_info=Firma.objects.get(meno_firmy="Mangalis")
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'home/index.html',
        context={'mangalis_info': mangalis_info},
    )