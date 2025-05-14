from rest_framework import serializers
from medication.models import Medication, MedicationSchedule, MedicationLog, DailyNote

class MedicationScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationSchedule
        fields = '__all__'

class MedicationSerializer(serializers.ModelSerializer):
    schedules = MedicationScheduleSerializer(many=True, read_only=True, source='medicationschedule_set')

    class Meta:
        model = Medication
        fields = ['id', 'name', 'is_active', 'default_dose_amount', 'default_dose_unit', 'schedules']

class MedicationLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedicationLog
        # fields = '__all__'
        exclude = 'user', 'medication_name', 'date', 'time'

class DailyNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyNote
        fields = '__all__'

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