from django.contrib.auth import get_user_model
from django.db import models

from eventsProject.eventar.models import Event
from eventsProject.utils import CharsValidator

UserModel = get_user_model()

class Comment(models.Model):
    author = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='comments_author',
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='comments_event',
    )

    content = models.TextField(
        validators=[CharsValidator()],
    )

    create_time = models.DateTimeField(
        auto_now_add=True,
    )

    last_edited = models.DateTimeField(
        auto_now=True,
    )

    edited = models.BooleanField(
        default=False,
    )

    is_deleted = models.BooleanField(
        default=False,
    )

    is_approved = models.BooleanField(
        default=True,
    )

    is_flagged = models.BooleanField(
        default=False,
    )


class CommentReaction(models.Model):
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name='reactions',
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='comment_reactions',
    )

    reaction_type = models.CharField(
        max_length=10,
        choices=[
            ('like', 'Like'),
            ('dislike', 'Dislike'),
        ],
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        unique_together = ('comment', 'user')

