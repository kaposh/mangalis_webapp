from django.shortcuts import render
from contact.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
def contact(request):
    """
    View function for contact page of site.
    """
    if request.method == 'GET':
        form = ContactForm()
        '''else:
    form = ContactForm(request.POST)
    if form.is_valid():
        subject = form.cleaned_data['subject']
        from_email = form.cleaned_data['from_email']
        message = form.cleaned_data['message']
        try:
            send_mail(subject, message, from_email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('success')'''
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'contact/contact.html',
        {'form': form},
)
