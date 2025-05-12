from django.db import models


class MedicationUseHistoryModel(models.Model):
    medication = models.ForeignKey('MedicationModel', on_delete=models.CASCADE, related_name="history")
    use_date = models.DateField(auto_now_add=True)
    use_time = models.TimeField(auto_now_add=True)
    dosage = models.FloatField(blank=True)
    dosage_type = models.CharField(max_length=30, blank=True)
