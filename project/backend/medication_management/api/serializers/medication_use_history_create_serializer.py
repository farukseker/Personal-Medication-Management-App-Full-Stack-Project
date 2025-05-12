from rest_framework import serializers
from medication_management.models import MedicationUseHistoryModel
from medication_management.models import MedicationModel
from django.shortcuts import get_object_or_404


class MedicationUseHistoryCreateSerializer(serializers.ModelSerializer):
    medication = serializers.PrimaryKeyRelatedField(queryset=MedicationModel.objects.all())

    class Meta:
        model: MedicationUseHistoryModel = MedicationUseHistoryModel
        fields: tuple = 'dosage', 'medication'

    def create(self, validated_data):
        medication = validated_data.get('medication')
        dosage_type = medication.dosage_type if medication else None
        instance = MedicationUseHistoryModel.objects.create(
            **validated_data,
            dosage_type=dosage_type
        )
        return instance