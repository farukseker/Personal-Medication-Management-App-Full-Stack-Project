from rest_framework import serializers
from medication.models import Medication, MedicationSchedule, MedicationLog, DailyNote



class SimpleMedicationScheduleSerializer(serializers.Serializer):
    medication_name = serializers.CharField()
    medication_id = serializers.IntegerField()
    dose = serializers.FloatField()  # veya DecimalField() kullanabilirsin
    unit = serializers.CharField()
    schedule_id = serializers.IntegerField()
    dose_time_id = serializers.IntegerField()
    time = serializers.TimeField()

    class Meta:
        ordering = 'time',
        # 12: 57