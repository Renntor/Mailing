from mail.apps import MailConfig
from django.urls import path
from mail.views import ClientListView, ClientCreateView

app_name = MailConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='home'),
    path('create_client/', ClientCreateView.as_view(), name='create_client'),

]
