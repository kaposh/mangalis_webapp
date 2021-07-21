# make sure this is at the top if it isn't already
from django import forms

# our new form
class ContactForm(forms.Form):
    sender_name = forms.CharField(label='Meno odosielateľa', required=True, widget=forms.TextInput(attrs={'placeholder': 'Zadajte vaše meno', 'class' : 'formfield'}))
    contact_email = forms.EmailField(label='Kontaktný email',required=True, widget=forms.TextInput(attrs={'placeholder': 'Zadajte váš email', 'class' : 'formfield'}))
    content = forms.CharField(label='Obsah', required=True, widget=forms.Textarea(attrs={'placeholder': 'Ako vám môžeme pomôcť?','class' : 'formfield','style':'resize:none;'}))