from django.contrib import admin
from users.models import User
from django.contrib.auth import models


# Register your models here.

# class StaffAdmin(admin.ModelAdmin):
#     """Права менеджера"""
#
#
#
#     def has_change_permission(self, request, obj=None):
#         if request.user.is_superuser:
#             self.exclude = ('mail_key', 'password')
#             return True
#         else:
#             self.fields = ('is_active',)
#             return True


admin.site.register(User)
