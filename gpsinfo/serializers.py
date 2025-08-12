# app/serializers.py
from rest_framework import serializers
from .models import GPSLocation

class GPSLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPSLocation
        fields = ['id', 'latitude', 'longitude', 'timestamp', 'altitude', 'accuracy', 'user']
        read_only_fields = ['timestamp', 'user']