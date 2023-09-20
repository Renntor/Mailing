from users.forms import StyleFormMixin
from django import forms
from mail.models import Client, SettingMail, Mailing
from django.contrib.admin import widgets


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        exclude = ('owner',)


class SettingMailForm(StyleFormMixin, forms.ModelForm):
    # mailing_time = forms.SplitDateTimeField(widget=widgets.AdminSplitDateTime)
    client = forms.ModelMultipleChoiceField(queryset=Client.objects.filter(email='denis305@yandex.ru'), required=False)

    class Meta:
        model = SettingMail
        fields = ('client' ,'mailing_time', 'period', 'status',)


class MailingForm(StyleFormMixin, forms.ModelForm):
    setting = forms.ModelMultipleChoiceField(queryset=SettingMail.objects.filter(status=True), required=False)

    class Meta:
        model = Mailing
        fields = ('setting', 'subject', 'text',)



