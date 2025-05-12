from django.db import models


class MedicationReminderModel(models.Model):
    medication = models.ForeignKey('MedicationModel', on_delete=models.CASCADE, related_name="reminder")
    time = models.TimeField()
