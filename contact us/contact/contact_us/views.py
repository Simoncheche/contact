from .forms import ContactForm
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

def contact_us(request):  
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        #name = request.POST['name']
        send_mail(
            'conatact Form',
            message,
            'settings.EMAIL_HOST_USER',
            [email,'@gmail.com', ''],
            fail_silently=False)
        form = ContactForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('contact_us')
    else:
        form = ContactForm() 
    return render(request, 'contact_us/contact_us.html', {'form': form})


