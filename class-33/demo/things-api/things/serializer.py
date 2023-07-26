from rest_framework import serializers
from .models import Thing


class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'owner', 'name', 'description', 'updated_at', 'created_at')
        model = Thing
