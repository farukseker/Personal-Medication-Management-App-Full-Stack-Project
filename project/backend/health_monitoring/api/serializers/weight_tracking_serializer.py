from rest_framework import serializers
from health_monitoring.models import WeightEntry


class WeightEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightEntry
        fields = ['id', 'weight', 'date']
