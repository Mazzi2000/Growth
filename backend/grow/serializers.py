from rest_framework import serializers
from .models import Grow

class GrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grow
        fields = ['id', 'name', 'description', 'completed']