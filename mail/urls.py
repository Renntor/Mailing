from mail.apps import MailConfig
from django.urls import path
from mail.views import ClientListView, ClientCreateView, SettingMailDetailView, SettingMailListView, SettingMailCreateView, ClientUpdateView, SettingUpdateView

app_name = MailConfig.name

urlpatterns = [
    path('', ClientListView.as_view(), name='home'),
    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('list_setting/', SettingMailListView.as_view(), name='list_setting'),
    path('create_setting/', SettingMailCreateView.as_view(), name="create_setting"),
    path('edit/<int:pk>', ClientUpdateView.as_view(), name='edit_client'),
    path('list_setting/edit/<int:pk>', SettingUpdateView.as_view(), name='edit_setting'),
    # path('list_setting/<int:pk>/', SettingMailDetailView.as_view(), name='list_setting'),

]
