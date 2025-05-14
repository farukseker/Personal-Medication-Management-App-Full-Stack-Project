from rest_framework import serializers
from medication.models import DailyNote




class DailyNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyNote
        fields = '__all__'