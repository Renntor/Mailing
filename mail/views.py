from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from mail.forms import ClientForm, SettingMailForm, MailingForm
from mail.models import Client, SettingMail, Mailing, Log
from django.contrib.auth.mixins import LoginRequiredMixin


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mail:home')


class ClientListView(ListView):
    model = Client
    template_name = 'mail/home.html'


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mail:home')


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client


class SettingMailListView(LoginRequiredMixin, ListView):
    model = SettingMail


class SettingMailCreateView(LoginRequiredMixin, CreateView):
    model = SettingMail
    form_class = SettingMailForm
    success_url = reverse_lazy('mail:list_setting')


class SettingUpdateView(LoginRequiredMixin, UpdateView):
    model = SettingMail
    form_class = SettingMailForm
    success_url = reverse_lazy('mail:list_setting')


class SettingMailDeleteView(LoginRequiredMixin, DeleteView):
    model = SettingMail


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mail:list_mail')


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mail:list_mail')


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing


class LogListView(LoginRequiredMixin, ListView):
    model = Log
