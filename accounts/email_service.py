from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


def welcome_email_new_user(user):
    message = render_to_string('accounts/email_templates/welcome_new_user.html', {
        'user': user,
    })
    mail_subject = 'موفقیت ثبت نام'
    email = EmailMessage(
        mail_subject, message, to=[user.email]
    )
    email.send()
