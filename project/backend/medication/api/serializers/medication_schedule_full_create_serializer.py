from rest_framework import serializers
from medication.models import MedicationSchedule, Medication
from .medication_dose_time_serializer import MedicationDoseTimeSerializer
from .medication_serializer import MedicationSerializer

# MedicationScheduleCreateSerializer
class MedicationScheduleCreateSerializer(serializers.ModelSerializer):
    medication_dose_times = MedicationDoseTimeSerializer(many=True, required=False)
    medication = MedicationSerializer()

    def create(self, validated_data):
        print(validated_data)

    class Meta:
        model = MedicationSchedule
        fields = '__all__'
