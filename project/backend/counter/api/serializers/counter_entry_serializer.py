from rest_framework import serializers
from counter.models import CounterEntry


class CounterEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = CounterEntry
        fields: str = '__all__'
