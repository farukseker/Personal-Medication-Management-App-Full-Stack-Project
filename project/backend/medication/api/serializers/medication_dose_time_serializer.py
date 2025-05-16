from rest_framework import serializers
from medication.models import MedicationDoseTime


class MedicationDoseTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationDoseTime
        fields = ['time', 'dose_amount', 'dose_unit']
