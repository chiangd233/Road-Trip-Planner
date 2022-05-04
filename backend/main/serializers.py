from rest_framework import serializers
from .models import RoadTrip, Location

class RoadTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadTrip
        fields = ('id', 'name', 'time', 'location')