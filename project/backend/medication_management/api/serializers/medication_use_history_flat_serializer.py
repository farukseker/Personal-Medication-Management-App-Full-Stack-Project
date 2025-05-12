from rest_framework import serializers
from medication_management.models import MedicationUseHistoryModel


class MedicationUseHistoryFlatSerializer(serializers.ModelSerializer):
    medication_name = serializers.CharField(source='medication.name')

    class Meta:
        model = MedicationUseHistoryModel
        fields = ['id', 'use_date', 'use_time', 'dosage', 'dosage_type', 'medication_name']
