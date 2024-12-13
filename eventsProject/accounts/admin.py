from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from eventsProject.accounts.forms import BaseUserCreationForm, BaseUserChangeForm

UserModel = get_user_model()

@admin.register(UserModel)
class BaseCustomUserAdmin(UserAdmin):
    model = UserModel
    add_form = BaseUserCreationForm
    form = BaseUserChangeForm

    list_display = ('email', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_active', 'date_joined')
    search_fields = ('email',)
    ordering = ('email',)
    readonly_fields = ('date_joined', 'last_login')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ()}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
        (_('Important Dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff'),
        }),
    )

