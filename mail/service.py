import random

from mail.models import Mailing, Log, SettingMail
from blog.models import Blog
from django.core.mail import send_mail
from django.conf import settings
import datetime


def _send_mail(subject: str, text: str, mail: list) -> None:
    send_mail(
        subject,
        text,
        settings.EMAIL_HOST_USER,
        [mail]
    )


def shipment_check():
    datetime_now = datetime.datetime.now(datetime.timezone.utc)

    mails = Mailing.objects.all()

    for mail in mails:
        if mail.setting.status == True:
            last_mail = Log.objects.filter(mail=mail, setting=mail.setting, status_try='finish').last()
            if last_mail:
                if (datetime_now - last_mail.date_last_try).days >= mail.setting.period:
                    _send_mail(mail.subject, mail.text, mail.setting.client.email)
                    Log.objects.create(mail=mail, setting=mail.setting, date_last_try=datetime_now, status_try='finish')
            else:
                _send_mail(mail.subject, mail.text, mail.setting.client.email)
                Log.objects.create(mail=mail, setting=mail.setting, date_last_try=datetime_now, status_try='finish')


def random_blog() -> list:
    """
    Возвращает список из 3 случайных статей
    """
    return Blog.objects.order_by('?')[:3]