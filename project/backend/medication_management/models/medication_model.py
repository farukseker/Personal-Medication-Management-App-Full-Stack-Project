from django.db import models
from django.contrib.postgres.fields import ArrayField


class MedicationModel(models.Model):
    name = models.CharField(
        max_length=255,
        help_text='ilacın adı'
    )
    notes = models.CharField(
        max_length=500,
        help_text='bu ilaç için bit not ekleyin (opsiyonel)',
        blank=True
    )
    hunger_situation = models.CharField(
        max_length=10,
        default='non', # Fark etmez
        help_text='Açlık durumu (Fark etmez|aç|tok)',
    )
    start_date = models.DateField(null=True, blank=True, help_text='Varsa ilaca başlama Tarihi')
    end_date = models.DateField(null=True, blank=True, help_text='Varsa bitiş tarihi')

    stages = models.ManyToManyField('StageSteps')
    often = ArrayField(models.CharField(max_length=50))
    # history = models.ManyToManyField('MedicationUseHistoryModel')

    @property
    def dosage(self):
        stage = self.stages.first()
        return stage.unit if stage else None

    @property
    def dosage_type(self):
        stage = self.stages.first()
        return stage.unit_type if stage else None

