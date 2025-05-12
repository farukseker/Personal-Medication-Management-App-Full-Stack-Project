from rest_framework import serializers
from medication_management.models import MedicationUseHistoryModel


class MedicationUseHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model: MedicationUseHistoryModel = MedicationUseHistoryModel
        fields: str = '__all__'
