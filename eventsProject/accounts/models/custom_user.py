import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

from cloudinary.models import CloudinaryField

from eventsProject.utils import ImageFileValidator, CharsValidator

UserModel = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    display_name = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        validators=[CharsValidator(), ]
    )

    bio = models.TextField(
        blank=True,
        null=True,
        validators=[CharsValidator(),]
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

    slug = models.SlugField(
        unique=True,
        editable=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    def delete(self, *args, **kwargs):
        self.is_active = False
        self.user.delete()
        self.save()

    def reactivate(self):
        self.is_active = True
        self.user.reactivate()
        self.save()

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
        indexes = [
            models.Index(fields=['slug']),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            nick = slugify(str(self.user.email.split('@')[0][:6]))
            nick = nick.replace('_', '-')
            self.slug = f"{nick}-{uuid.uuid4().hex}"
        super().save(*args, **kwargs)

    def __str__(self):
        if not self.is_active:
            user_display_name = "Deleted User"
        elif self.display_name:
            user_display_name = self.display_name
        else:
            user_display_name = self.user.email

        return user_display_name if user_display_name else "Anonymous User"
