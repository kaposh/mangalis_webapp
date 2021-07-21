from contact.models import Firma
from django.shortcuts import  get_object_or_404

def add_variable_to_context(request):
    #mangalis_info = Firma.objects.get(meno_firmy="Mangalis")
    mangalis_info = get_object_or_404(Firma, meno_firmy="Mangalis")
    return {
        'mangalis_info': mangalis_info
    }