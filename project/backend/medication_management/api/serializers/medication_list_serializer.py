from rest_framework import serializers
from medication_management.models import MedicationModel, StageSteps
from .stage_serializer import StageStepsSerializer
from .medication_use_history_serializer import MedicationUseHistorySerializer


class MedicationListSerializer(serializers.ModelSerializer):
    stages = StageStepsSerializer(many=True)
    often = serializers.ListField(child=serializers.CharField())
    history = MedicationUseHistorySerializer(many=True)

    class Meta:
        model: MedicationModel = MedicationModel
        fields: str = '__all__'
