from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
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

    parent = models.ForeignKey(
        'self',
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name='replies',
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

    @property
    def display_content(self):
        return "[Deleted]" if self.is_deleted else self.content

    def __str__(self):
        author_identifier = self.author.user.display_name if self.author.user.display_name else self.author.email
        return f"{author_identifier} - {self.content}"

    def soft_delete(self):
        self.is_deleted = True
        self.is_approved = False
        self.save(update_fields=['is_deleted', 'is_approved'])

    def clean(self):
        if self.is_deleted:
            raise ValidationError("Cannot edit a deleted comment.")

        if self.is_flagged:
            raise ValidationError("Cannot edit a flagged comment.")

        if self.parent == self:
            raise ValidationError("A comment cannot be its own parent.")

        if self.parent and self.parent.event != self.event:
            raise ValidationError("A reply must belong to the same event as its parent.")

        super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def delete(self, * args, **kwargs):
        self.soft_delete()


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
        constraints = [
            models.UniqueConstraint(fields=['comment', 'user'], name='unique_comment_reaction')
        ]
