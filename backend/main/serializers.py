from rest_framework import serializers
from .models import RoadTrip, ThingsTodo

class RoadTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadTrip
        fields = ('id', 'name', 'time', 'thingstodo', 'routes', 'created_at', 'user')

class ThingsTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThingsTodo
        fields = ('id', 'name', 'state')