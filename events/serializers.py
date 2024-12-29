from rest_framework import serializers
from .models import Events


class BulkEventsSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        Events = [Events(**item) for item in validated_data]
        return Events.objects.bulk_create(Events)


class EventsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Events
        fields = '__all__'
        list_serializer_class = BulkEventsSerializer
        
    def create(self, validated_data):
        return Events.objects.create(**validated_data)