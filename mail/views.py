from django.forms import inlineformset_factory
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from mail.forms import ClientForm, SettingMailForm, MailingForm
from mail.models import Client, SettingMail, Mailing, Log
from django.contrib.auth.mixins import LoginRequiredMixin


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
    template_name = 'mail/home.html'


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mail:home')


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('mail:home')


class SettingMailListView(LoginRequiredMixin, ListView):
    model = SettingMail


class SettingMailCreateView(LoginRequiredMixin, CreateView):
    model = SettingMail
    form_class = SettingMailForm
    success_url = reverse_lazy('mail:list_setting')

    def form_valid(self, form):
        self.object = form.save()
        owner = Client.objects.filter(email=self.request.user)[0]
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


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        qs = [i for i in SettingMail.objects.all() if i.status == True]
        context['setting'] = qs
        return context


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mail:list_mail')


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('mail:list_mail')


class LogListView(LoginRequiredMixin, ListView):
    model = Log
