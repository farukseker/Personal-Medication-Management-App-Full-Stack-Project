from django.db import models


class MedicationDoseTime(models.Model):
    # Her doz zamanı için kayıt (örn. sabah 08:00'de 1 tablet)
    schedule = models.ForeignKey('medication.MedicationSchedule', on_delete=models.CASCADE, related_name='dose_times')
    time = models.TimeField()           # Örneğin sabah 08:00
    dose_amount = models.FloatField()  # Örneğin 1.0
    dose_unit = models.CharField(max_length=20)  # Örneğin 'tablet'

    class Meta:
        unique_together = ('schedule', 'time')  # Aynı programda aynı saati tekrar girilmesin
