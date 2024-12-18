from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import UserProfile
from ..utils import AllowedFormatsMixin

UserModel = get_user_model()

class BaseUserChangeForm(UserChangeForm, AllowedFormatsMixin):
    class Meta(UserChangeForm.Meta):
        model = UserModel


class BaseUserCreationForm(UserCreationForm, AllowedFormatsMixin):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)


class CustomUserEditForm(forms.ModelForm, AllowedFormatsMixin):
    class Meta:
        model = UserProfile
        exclude = ('user', )