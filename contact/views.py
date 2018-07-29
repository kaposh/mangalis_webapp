from django.shortcuts import render
# Create your views here.
def contact(request):
    """
    View function for contact page of site.
    """
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'contact/contact.html',
        context={},
    )
