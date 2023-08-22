from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from mail.models import Client, SettingMail, Mailing, Log
from django.shortcuts import get_object_or_404

# Create your views here.


class ClientCreateView(CreateView):
    model = Client
    fields = ('full_name', 'email', 'comment')
    success_url = reverse_lazy('mail:home')


class ClientListView(ListView):
    model = Client
    template_name = 'mail/home.html'


class ClientUpdateView(UpdateView):
    model = Client
    fields = ('full_name', 'email', 'comment')
    success_url = reverse_lazy('mail:home')


class ClientDeleteView(DeleteView):
    model = Client


class SettingMailListView(ListView):
    model = SettingMail


class SettingMailCreateView(CreateView):
    model = SettingMail
    fields = ('client', 'mailing_time', 'period')
    success_url = reverse_lazy('mail:list_setting')


class SettingUpdateView(UpdateView):
    model = SettingMail
    fields = ('client', 'mailing_time', 'period')
    success_url = reverse_lazy('mail:list_setting')


class SettingMailDeleteView(DeleteView):
    model = SettingMail


class MailingListView(ListView):
    model = Mailing


class MailingCreateView(CreateView):
    model = Mailing
    fields = ('setting', 'subject', 'text')
    success_url = reverse_lazy('mail:list_mail')


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = ('setting', 'subject', 'text')
    success_url = reverse_lazy('mail:list_mail')


class MailingDeleteView(DeleteView):
    model = Mailing
