from rest_framework import serializers
from medication.models import MedicationSchedule, MedicationDoseTime
from .medication_dose_time_serializer import MedicationDoseTimeSerializer

class MedicationScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationSchedule
        fields = '__all__'


class MedicationCreateScheduleSerializer(serializers.ModelSerializer):
    dose_times = MedicationDoseTimeSerializer(many=True, required=False)

    class Meta:
        model = MedicationSchedule
        fields = [
            'start_date', 'end_date', 'frequency', 'interval', 'days_of_week',
            'day_of_month', 'doses_per_period', 'dose_amount', 'dose_unit', 'dose_times'
        ]
