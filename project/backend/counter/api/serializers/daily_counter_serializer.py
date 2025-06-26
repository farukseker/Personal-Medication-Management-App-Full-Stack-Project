from rest_framework import serializers


class DailyCounterSerializer(serializers.Serializer):
    date = serializers.DateField()
    counter_id = serializers.IntegerField()
    counter_name = serializers.CharField(source='counter__name')
    total = serializers.IntegerField()
