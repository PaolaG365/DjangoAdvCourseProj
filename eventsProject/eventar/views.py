from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from eventsProject.eventar.models import Event
from eventsProject.eventar.serializers import EventSerializer


class EventView(RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

