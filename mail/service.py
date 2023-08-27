from mail.models import Mailing
from django.core.mail import send_mail
from django.conf import settings


def _send_mail(subject, text, mail):
    send_mail(
        subject,
        text,
        settings.EMAIL_HOST_USER,
        [mail]
    )


