from cloudinary.forms import CloudinaryFileField, CloudinaryInput
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import UserProfile
from ..utils import AllowedFormatsMixin, ImageFileValidator

UserModel = get_user_model()


class BaseUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel


class BaseUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)


class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user', )
        picture = CloudinaryFileField()
        help_texts = {
            'picture': 'Upload a picture, allowed formats: jpg, jpeg, png, gif, webp'
        }
