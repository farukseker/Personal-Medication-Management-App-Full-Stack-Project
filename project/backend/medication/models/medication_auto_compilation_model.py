from django.db import models


class MedicationAutoCompilationModel(models.Model):
    name = models.CharField(max_length=255)
    barcode = models.CharField(max_length=30, blank=True)
    value = models.CharField(max_length=30, blank=True)
    unit = models.CharField(max_length=30, blank=True)
