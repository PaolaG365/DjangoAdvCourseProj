from django.contrib.auth import get_user_model
from django.db import models

from cloudinary.models import CloudinaryField

from eventsProject.utils import ImageFileValidator

UserModel = get_user_model()


class CustomUser(models.Model):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    display_name = models.CharField(
        max_length=150,
        blank=True,
    )

    bio = models.TextField(
        blank=True,
    )

    picture = CloudinaryField(
        'image',
        null=True,
        blank=True,
        validators=[ImageFileValidator(),]
    )

    location =  models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )

    date_created = models.DateTimeField(
        auto_now_add=True,
    )

    last_updated = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        if self.display_name:
            user_display_name = self.display_name
        else:
            user_display_name = self.user.email

        return user_display_name if user_display_name else "Anonymous User"
