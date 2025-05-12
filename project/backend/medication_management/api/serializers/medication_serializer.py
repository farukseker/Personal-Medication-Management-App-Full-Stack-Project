from rest_framework import serializers
from medication_management.models import MedicationModel, StageSteps
from .stage_serializer import StageStepsSerializer


class MedicationModelSerializer(serializers.ModelSerializer):
    stages = StageStepsSerializer(many=True)
    often = serializers.ListField(child=serializers.CharField())

    class Meta:
        model: MedicationModel = MedicationModel
        fields: str = '__all__'

    def create(self, validated_data):
        stages_data = validated_data.pop('stages')
        medication = MedicationModel.objects.create(**validated_data)
        for stage_data in stages_data:
            stage = StageSteps.objects.create(**stage_data)
            medication.stages.add(stage)
        return medication