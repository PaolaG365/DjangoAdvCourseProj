from django.contrib.auth import get_user_model
from django.db import models

from cloudinary.models import CloudinaryField

from .event_model import Event
from eventsProject.utils import CharsValidator, ImageFileValidator, VideoFileValidator

UserModel = get_user_model()

class EventImage(models.Model):
    event = models.ForeignKey(
        Event,
        related_name='event_gallery_images',
        on_delete=models.CASCADE,
    )

    image = CloudinaryField(
        'image',
        validators=[ImageFileValidator()],
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True,
    )

    def __str__(self):
        return f'Image for {self.event.title}'


class EventVideo(models.Model):
    event = models.ForeignKey(
        Event,
        related_name='event_gallery_videos',
        on_delete=models.CASCADE,
    )

    video = CloudinaryField(
        'video',
        validators=[VideoFileValidator()],
    )

    uploaded_at = models.DateTimeField()

    def __str__(self):
        return f'Video for {self.event.title}'


# TODO: automated emails with celery
class Reminder(models.Model):
    content = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        validators=[CharsValidator(),]
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='reminders_user',
    )

    event = models.ForeignKey(
        Event,
        related_name='reminders_event',
        on_delete=models.CASCADE,
    )

    reminder_time = models.DateTimeField(
        help_text='Set when you want us to send you a reminder email for your event.',
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )
