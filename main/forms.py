from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    email = forms.CharField(label='email')
    phone = forms.CharField(label='phone')