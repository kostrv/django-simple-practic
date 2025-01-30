from django.shortcuts import render
from .forms import ContactForm


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

def process_feedback(request): 
    if request.method == 'POST': 
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            
            print(f'\nRequest:\nName: {name}\nEmail: {email}\nPhone: {phone}\n')
            return render(request, 'feedback.html', {'name': name})
    else:
        return render(request, 'required.html')
    