from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.template.loader import render_to_string, get_template 
from django.conf import settings
from crm.models import Record

def sendmail(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            subject = form.cleaned_data['subject']
            category = form.cleaned_data['category']
            message = form.cleaned_data['message']
            
            if category == "all":
                records = Record.objects.all()
            else:
                records = Record.objects.filter(category=category)

            for record in records:
                email_address = record.email
                context = {
                    'name': record.full_name,
                    'message': message,
                }
                email_template = get_template('sendmail/email.html').render(context)
                email = EmailMessage(subject, email_template, "CCRM 4.2 updates", [email_address])
                email.content_type = "html"
                email.send()
            return redirect('sendmail')

    return render(request, 'sendmail/sendmail.html', {'form': form})
