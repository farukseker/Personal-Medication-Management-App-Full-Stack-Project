from rest_framework import serializers
from medication_management.models import StageSteps


class StageStepsSerializer(serializers.ModelSerializer):
    class Meta:
        model: StageSteps = StageSteps
        fields: str = '__all__'
