from django.core.mail import EmailMessage
from celery import shared_task
from django.template.loader import render_to_string


@shared_task()
def welcome_email_new_user(email, first_name):
    message = render_to_string('accounts/email_templates/welcome_new_user.html', {
        'first_name': first_name,
    })
    mail_subject = 'موفقیت ثبت نام'
    email = EmailMessage(
        mail_subject, message, to=[email]
    )
    email.send()
