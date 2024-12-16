from django.utils.timezone import now

from rest_framework import serializers

from eventsProject.eventar.models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    # noinspection PyMethodMayBeStatic
    def validate_time_of_event(self, value):
        if value <= now():
            raise serializers.ValidationError("Time of event must be in the future.")

        return value
