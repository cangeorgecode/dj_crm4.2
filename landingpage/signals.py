from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.conf import settings
from .models import Lead

@receiver(post_save, sender=Lead)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Here is your freebies!'
        message = f'Hello {instance.full_name},\n\nWe are so excited to have you onboard!'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [instance.email]
        send_mail(subject, message, from_email, recipient_list)