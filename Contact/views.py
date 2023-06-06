from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            cd=form.cleaned_data
            email_subject = f'New contact {cd["email"]}: {cd["subject"]}'
            email_message = cd['message']
            send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAILS, fail_silently=False)
            return render(request, 'success.html')
    form = ContactForm()
    context = ({'form':form})

    return render(request,
                    'contact.html',context)

# Create your views here.
