from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'event', 'content', 'create_time', 'last_edited', 'edited', 'is_deleted')
    search_fields = ('author__email', 'content')
    list_filter = ('create_time', 'edited', 'is_deleted')