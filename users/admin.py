from django.contrib import admin
from users.models import User
from django.contrib.auth import models

# Register your models here.

class Staff(admin.ModelAdmin):
    """Права менеджера"""

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return request.user.is_superuser
        # else:
        #     self.readonly_fields = list(
        #         set([field.name for field in self.opts.local_fields if field.name != 'is_active']))
        #     return True


admin.site.register(User, Staff)
