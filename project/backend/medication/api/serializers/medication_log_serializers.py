from rest_framework import serializers
from medication.models import MedicationLog



class MedicationLogCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedicationLog
        # fields = '__all__'
        exclude = 'user', 'medication_name', 'date', 'time'


class MedicationLogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationLog
        fields = '__all__'


class MedicationLogSplitListSerializer(serializers.Serializer):
    medication_logs = MedicationLogListSerializer(many=True, read_only=True)
    date = serializers.DateField()
