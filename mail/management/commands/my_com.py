from mail.service import _send_mail
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        _send_mail()
