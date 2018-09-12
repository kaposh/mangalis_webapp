from contact.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.
def contact(request):
    """
    View function for contact page of site.
    """
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['sender_name']
            from_email = form.cleaned_data['contact_email']
            message = form.cleaned_data['content']
            try:
                send_mail("Mangalis email: "+subject, message, from_email, ['marek.bohdan1@gmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            ContactForm()
            return redirect('/contact/success')
    # Render the HTML template index.html with the data in the context variable
    return render(request,'contact/contact.html',{'form': form},)

def success(request):
    return render(request, 'contact/success.html')