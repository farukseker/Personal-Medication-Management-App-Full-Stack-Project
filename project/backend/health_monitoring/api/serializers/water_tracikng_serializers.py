from rest_framework import serializers
from health_monitoring.models import WaterEntry, WaterGoal


class WaterEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterEntry
        fields = ['id', 'amount', 'timestamp']


class WaterGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterGoal
        fields = ['daily_goal']
