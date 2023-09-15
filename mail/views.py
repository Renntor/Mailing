from django.forms import inlineformset_factory
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from mail.forms import ClientForm, SettingMailForm, MailingForm
from mail.models import Client, SettingMail, Mailing, Log
from django.contrib.auth.mixins import LoginRequiredMixin

from mail.service import random_blog


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mail:home')

    def form_valid(self, form):
        self.object = form.save()
        self.object.client = self.request.user
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class ClientListView(ListView):
    model = Client


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mail:client')


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mail:client')


class SettingMailListView(LoginRequiredMixin, ListView):
    model = SettingMail


class SettingMailCreateView(LoginRequiredMixin, CreateView):
    model = SettingMail
    form_class = SettingMailForm
    success_url = reverse_lazy('mail:list_setting')

    def form_valid(self, form):
        self.object = form.save()
        owner = Client.objects.get(email=self.request.user)
        self.object.client = owner
        self.object.save()

        return super().form_valid(form)


class SettingUpdateView(LoginRequiredMixin, UpdateView):
    model = SettingMail
    form_class = SettingMailForm
    success_url = reverse_lazy('mail:list_setting')


class SettingMailDeleteView(LoginRequiredMixin, DeleteView):
    model = SettingMail
    success_url = reverse_lazy('mail:list_setting')


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
    success_url = reverse_lazy('mail:list_mail')


class LogListView(LoginRequiredMixin, ListView):
    model = Log


def title(request):
    context = {'blog_list': random_blog(),
               'count_mailing': len(Log.objects.filter(status_try='finish')),
               'count_active': len(SettingMail.objects.filter(status=True)),
               'count_client': len(Client.objects.all())}
    return render(request, 'mail/home.html', context=context)