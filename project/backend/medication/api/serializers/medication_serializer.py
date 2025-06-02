from rest_framework import serializers
from medication.models import Medication, MedicationSchedule, MedicationDoseTime
from .medication_schedule_serializer import MedicationScheduleSerializer, MedicationCreateScheduleSerializer


class MedicationSerializer(serializers.ModelSerializer):
    schedules = MedicationScheduleSerializer(many=True, read_only=True)


    class Meta:
        model = Medication
        fields = ['id', 'name', 'is_active', 'default_dose_amount', 'default_dose_unit', 'schedules']


class MedicationCreateSerializer(serializers.ModelSerializer):
    schedules = MedicationCreateScheduleSerializer(many=True, required=False)

    class Meta:
        model = Medication
        fields = ['id', 'name', 'is_active', 'default_dose_amount', 'default_dose_unit', 'schedules']

    def create(self, validated_data):
        schedules_data = validated_data.pop('schedules', [])
        validated_data['user'] = self.context['request'].user  # override güvenli olsun

        medication = Medication.objects.create(**validated_data)

        for schedule_data in schedules_data:
            dose_times_data = schedule_data.pop('dose_times', [])
            days_of_week_data = schedule_data.pop("days_of_week", [])

            schedule = MedicationSchedule.objects.create(medication=medication, **schedule_data)
            schedule.days_of_week.set(days_of_week_data)
            for dose_data in dose_times_data:
                MedicationDoseTime.objects.create(schedule=schedule, **dose_data)

        return medication

    def update(self, instance, validated_data):
        schedules_data = validated_data.pop('schedules', None)

        # Ana verileri güncelle
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if schedules_data is not None:
            # Tüm eski schedule'ları sil (gerekirse daha akıllı diff uygulanabilir)
            instance.schedules.all().delete()

            for schedule_data in schedules_data:
                dose_times_data = schedule_data.pop('dose_times', [])
                days_of_week_data = schedule_data.pop("days_of_week", [])

                schedule = MedicationSchedule.objects.create(medication=instance, **schedule_data)
                schedule.days_of_week.set(days_of_week_data)
                for dose_data in dose_times_data:
                    MedicationDoseTime.objects.create(schedule=schedule, **dose_data)

        return instance
