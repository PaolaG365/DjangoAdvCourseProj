from django import forms
from django.core.validators import FileExtensionValidator


class AllowedFormatsMixin:
    def add_allowed_formats(self):
        for field_name, field in self.fields.items():
            if isinstance(field, forms.FileField):
                validators = getattr(field, "validators", [])

                for validator in validators:
                    if getattr(validator, "ALLOWED_EXTENSIONS", None):
                        allowed_formats = ", ".join(validator.ALLOWED_EXTENSIONS)
                        help_text = f"Allowed formats: {allowed_formats}"

                        field.help_text += f" ({help_text})" if field.help_text else help_text

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_allowed_formats()
