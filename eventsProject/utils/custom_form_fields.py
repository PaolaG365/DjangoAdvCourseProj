from django import forms
from .validators import ImageFileValidator  # Adjust path as necessary


class CustomImageField(forms.ImageField):
    def clean(self, data, initial=None):
        data = super().clean(data, initial)

        validator = ImageFileValidator()
        validator(data)

        return data
