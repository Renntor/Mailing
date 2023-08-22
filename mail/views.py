from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.core.mail import send_mail
from django.urls import reverse_lazy
from mail.models import Client, SettingMail, Mailing, Log

# Create your views here.


class ClientCreateView(CreateView):
    model = Client
    fields = ('full_name', 'email', 'comment')
    success_url = reverse_lazy('mail:home')


class ClientListView(ListView):
    model = Client
    template_name = 'mail/home.html'


class ClientDetailView(DetailView):
    model = Client


class ClientUpdateView(UpdateView):
    model = Client


class ClientDeleteView(DeleteView):
    model = Client


