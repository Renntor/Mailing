from mail.models import Mailing, Log, SettingMail
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
        if mail.setting.status == 'create':
            _send_mail(mail.subject, mail.text, mail.setting.client.email)
            Log.objects.create(mail=mail, setting=mail.setting, date_last_try=datetime_now, status_try='finish')
            mail.setting.status = 'start'
            mail.setting.save()
        last_mail = Log.objects.filter(mail=mail, setting=mail.setting, status_try='finish').last()
        if last_mail.setting.status == 'finish':
            last_mail.status_try = 'close'
            last_mail.save()
        elif (datetime_now - last_mail.date_last_try).days >= last_mail.setting.period:
            _send_mail(mail.subject, mail.text, mail.setting.client.email)
            Log.objects.create(mail=mail, setting=mail.setting, date_last_try=datetime_now, status_try='finish')
