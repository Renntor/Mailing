from users.forms import StyleFormMixin
from django import forms
from mail.models import Client, SettingMail, Mailing


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class SettingMailForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = SettingMail
        fields = ('client', 'mailing_time', 'period', 'status',)



class MailingForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Mailing
        fields = '__all__'
