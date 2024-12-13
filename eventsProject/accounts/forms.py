from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser

UserModel = get_user_model()

class BaseUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel


class BaseUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)


class CustomUserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        exclude = ('user', )