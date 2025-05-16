from rest_framework import serializers
from medication.models import Medication, MedicationSchedule, MedicationDoseTime
from .medication_schedule_serializer import MedicationScheduleSerializer, MedicationCreateScheduleSerializer
from .medication_dose_time_serializer import MedicationDoseTimeSerializer


class MedicationSerializer(serializers.ModelSerializer):
    schedules = MedicationScheduleSerializer(many=True, read_only=True)


    class Meta:
        model = Medication
        fields = ['id', 'name', 'is_active', 'default_dose_amount', 'default_dose_unit', 'schedules']


class MedicationCreateSerializer(serializers.ModelSerializer):
    schedules = MedicationCreateScheduleSerializer(many=True, required=False)
    dose_times = MedicationDoseTimeSerializer(many=True, required=False)

    class Meta:
        model = Medication
        fields = ['id', 'name', 'is_active', 'default_dose_amount', 'default_dose_unit', 'schedules', 'dose_times']

    def validate_schedules(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Schedules must be a list.")
        return value

    def validate_dose_times(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Schedules must be a list.")
        return value

    def create(self, validated_data):
        schedules_data = validated_data.pop('schedules', [])
        dose_times = validated_data.pop('dose_times', [])

        medication = Medication.objects.create(**validated_data)

        for dose_time_data in dose_times:
            MedicationDoseTime.objects.create(medication=medication, **dose_time_data)

        for schedule_data in schedules_data:
            days_of_week = schedule_data.pop('days_of_week', [])  # çıkar
            schedule = MedicationSchedule.objects.create(medication=medication, **schedule_data)
            schedule.days_of_week.set(days_of_week)  # many-to-many alan set edilir

        return medication

    def update(self, instance, validated_data):
        schedules_data = validated_data.pop('schedules', None)
        dose_times = validated_data.pop('dose_times', [])

        # Medication modelinin temel alanlarını güncelle
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Eğer schedules verisi gelmişse
        if schedules_data is not None:
            # Var olan tüm schedule'ları silip yeniden ekliyoruz (alternatifi matching ID ile güncellemek)
            instance.schedules.all().delete()
            for schedule_data in schedules_data:
                MedicationSchedule.objects.create(medication=instance, **schedule_data)

        return instance
