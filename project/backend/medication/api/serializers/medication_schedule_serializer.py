from rest_framework import serializers
from medication.models import MedicationSchedule


class MedicationScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationSchedule
        fields = '__all__'