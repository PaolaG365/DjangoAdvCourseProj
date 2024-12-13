from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Category, Event

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at")
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("created_at",)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "organizer", "time_of_event", "location", "category", "slug")
    search_fields = ("title", "organizer__display_name", "organizer__email", "location", "event_info")
    list_filter = ("time_of_event", "category", "tags")
    prepopulated_fields = {"slug": ("title",)}
    ordering = ("-time_of_event",)

    def get_queryset(self, request):
        # To ensure efficient queries
        return super().get_queryset(request).select_related("organizer", "category").prefetch_related("tags")
