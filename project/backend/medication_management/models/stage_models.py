from django.db import models


class StageSteps(models.Model):
    unit = models.FloatField(
        default=.0,
        help_text='ilacın gramajı'
    )
    unit_type = models.CharField(max_length=10)
    range_start_date = models.DateField()
    range_end_date = models.DateField()
    range_length = models.IntegerField(
        help_text='Aralık uzunlu'
    )
    range_type = models.CharField(
        max_length=10,
        help_text='Aralık tipi, (Gün|Hafta|Ay|Yıl)'
    )

