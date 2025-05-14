from rest_framework import serializers
from medication.models import Medication
from .medication_schedule_serializer import MedicationScheduleSerializer


class MedicationSerializer(serializers.ModelSerializer):
    schedules = MedicationScheduleSerializer(many=True, read_only=True, source='medicationschedule_set')

    class Meta:
        model = Medication
        fields = ['id', 'name', 'is_active', 'default_dose_amount', 'default_dose_unit', 'schedules']