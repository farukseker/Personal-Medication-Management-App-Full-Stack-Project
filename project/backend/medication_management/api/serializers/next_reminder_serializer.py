from rest_framework import serializers


class NextReminderSerializer(serializers.Serializer):
    medication_id = serializers.IntegerField()
    medication_name = serializers.CharField()
    scheduled_time = serializers.TimeField(format="%H:%M")
    taken_count = serializers.IntegerField()
    reminder_total = serializers.IntegerField()
    dosage = serializers.FloatField()
    dosage_type = serializers.CharField()
