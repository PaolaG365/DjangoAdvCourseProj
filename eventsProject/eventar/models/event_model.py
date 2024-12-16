from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

from taggit.managers import TaggableManager

from ...utils import CharsValidator

UserModel = get_user_model()


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        validators=[CharsValidator(),]
    )

    description = models.TextField(
        blank=True,
        null=True,
        validators=[CharsValidator(),]
    )

    slug = models.SlugField(
        max_length=60,
        unique=True,
        blank=True,
        help_text="URL-friendly identifier for the category. It must be unique.",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Event(models.Model):
    time_of_event = models.DateTimeField()

    title = models.CharField(
        max_length=100,
        validators=[CharsValidator(r'/^[a-zA-Z0-9\'\s]+$', 'Invalid title.')],
        help_text="The title of the event must contain only letters, digits, spaces or apostrophes."
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    last_updated = models.DateTimeField(
        auto_now=True,
    )

    event_info = models.TextField(
        blank=True,
        null=True,
        validators=[CharsValidator(),]
    )

    organizer = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        related_name="events_hosted",
        null=True,
    )

    location = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        validators=[CharsValidator(),]
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name="events_category",
        null=True,
    )

    slug = models.SlugField(
        max_length=120,
        unique=True,
        blank=True,
        help_text="URL-friendly identifier for the event. It must be unique."
    )

    # TODO: automated email when user adds an event to their list
    events_attendees = models.ManyToManyField(
        UserModel,
        related_name="attendees",
        blank=True,
    )

    tags = TaggableManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.time_of_event.date()}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Event: {self.title} Organizer: {self.organizer} Location: {self.location}"
