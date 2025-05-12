from rest_framework import serializers
from medication_management.models import MedicationAutoCompilationModel


class MedicationAutoCompilationModelSerializer(serializers.ModelSerializer):
    class Meta:
        model: MedicationAutoCompilationModel = MedicationAutoCompilationModel
        exclude: tuple = ('id' ,)
