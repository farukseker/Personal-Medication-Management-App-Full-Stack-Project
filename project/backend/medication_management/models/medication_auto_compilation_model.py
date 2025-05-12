from django.db import models


class MedicationAutoCompilationModel(models.Model):
    name = models.CharField(max_length=255)
    dosage = models.CharField(max_length=30, blank=True)
