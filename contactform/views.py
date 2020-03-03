from django.core.mail import BadHeaderError, send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.apps import apps 
from .decorators import check_recaptcha
from .forms import ContactForm

@check_recaptcha
def form(request):
    """ This view displays and processes the contact form """
    if request.method == 'GET':
        form = ContactForm()
    else: # Post request
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, email, [apps.get_app_config('Contactform').contact_form_recipient,])
            except BadHeaderError:
                messages.error(request, 'Invalid header found, please try again.')
            return redirect('contactform:success')

    return render(request, 'contactform/form.html', {
        'meta_title': 'Contact Form',
        'meta_description': 'Get in touch or open a support ticket.',
        'form': form
    })


def success(request):
    """ Displays the success page """
    return render(request, 'contactform/success.html', {
                            'meta_title': 'Thanks for your message',
                            'meta_description': 'Your message has been received, we\'ll reply as soon as possible.'})
