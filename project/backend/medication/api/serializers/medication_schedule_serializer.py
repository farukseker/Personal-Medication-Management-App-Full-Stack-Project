from rest_framework import serializers
from medication.models import MedicationSchedule, MedicationDoseTime
from .medication_dose_time_serializer import MedicationDoseTimeSerializer

class MedicationScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationSchedule
        fields = '__all__'


class MedicationCreateScheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedicationSchedule
        fields = ['start_date', 'end_date', 'frequency', 'interval', 'days_of_week',
                  'day_of_month', 'doses_per_period', 'dose_amount', 'dose_unit']
#
#     def create(self, validated_data):
#         dose_times_data = validated_data.pop('dose_times')
#         schedule = MedicationSchedule.objects.create(**validated_data)
#         for dose_data in dose_times_data:
#             MedicationDoseTime.objects.create(schedule=schedule, **dose_data)
#         return schedule
#
#     def update(self, instance, validated_data):
#         dose_times_data = validated_data.pop('dose_times')
#         # Schedule'ı güncelle
#         for attr, value in validated_data.items():
#             setattr(instance, attr, value)
#         instance.save()
#
#         # Önceki doz zamanlarını temizle, yeniden oluştur
#         instance.dose_times.all().delete()
#         for dose_data in dose_times_data:
#             MedicationDoseTime.objects.create(schedule=instance, **dose_data)
#
#         return instance
