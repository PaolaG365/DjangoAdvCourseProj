# Generated by Django 5.1.3 on 2024-12-12 22:35

import cloudinary.models
import django.db.models.deletion
import eventsProject.utils.validators
import taggit.managers
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, validators=[eventsProject.utils.validators.CharsValidator()])),
                ('description', models.TextField(blank=True, null=True, validators=[eventsProject.utils.validators.CharsValidator()])),
                ('slug', models.SlugField(blank=True, help_text='URL-friendly identifier for the category. It must be unique.', max_length=60, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_of_event', models.DateTimeField()),
                ('title', models.CharField(help_text='The title of the event must contain only letters, digits, spaces or apostrophes.', max_length=100, validators=[eventsProject.utils.validators.CharsValidator("/^[a-zA-Z0-9\\'\\s]+$", 'Invalid title.')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('event_info', models.TextField(blank=True, null=True, validators=[eventsProject.utils.validators.CharsValidator()])),
                ('location', models.CharField(blank=True, max_length=255, null=True, validators=[eventsProject.utils.validators.CharsValidator()])),
                ('slug', models.SlugField(blank=True, help_text='URL-friendly identifier for the event. It must be unique.', max_length=120, unique=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events_category', to='eventar.category')),
                ('events_attendees', models.ManyToManyField(blank=True, related_name='attendees', to=settings.AUTH_USER_MODEL)),
                ('organizer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events_hosted', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, validators=[eventsProject.utils.validators.ImageFileValidator()], verbose_name='image')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_gallery_images', to='eventar.event')),
            ],
        ),
        migrations.CreateModel(
            name='EventVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', cloudinary.models.CloudinaryField(max_length=255, validators=[eventsProject.utils.validators.VideoFileValidator()], verbose_name='video')),
                ('uploaded_at', models.DateTimeField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_gallery_videos', to='eventar.event')),
            ],
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=150, null=True, validators=[eventsProject.utils.validators.CharsValidator()])),
                ('reminder_time', models.DateTimeField(help_text='Set when you want us to send you a reminder email for your event.')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reminders_event', to='eventar.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reminders_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
