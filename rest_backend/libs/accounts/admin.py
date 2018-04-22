from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.utils.translation import ugettext_lazy as _
# Register your models here.


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('nickname', 'first_name', 'last_name',
                                         'phone', 'email', 'gender',
                                         'head_avatar', 'birthday',
                                         'description')}),
        (_('Permissions'), {'fields': ('is_active', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'nickname', 'phone', 'is_active',
                    'last_login')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'nickname', 'phone', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)
