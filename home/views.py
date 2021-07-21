from django.shortcuts import render
from contact.models import Firma

# Create your views here.
def index(request):
    """
    View function for home page of site.
    """
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'home/index.html',
        context={},
    )