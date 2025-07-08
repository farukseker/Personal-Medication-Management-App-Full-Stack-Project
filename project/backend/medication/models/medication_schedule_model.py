from django.db import models
from .medication_model import Medication
from .week_day_model import WeekDay


class MedicationSchedule(models.Model):
    FREQUENCY_CHOICES = [
        ('daily', 'Günlük'),
        ('weekly', 'Haftalık'),
        ('monthly', 'Aylık'),
        ('custom', 'Özel'),
    ]
    medication = models.ForeignKey('medication.Medication', on_delete=models.CASCADE, related_name='schedules')  # İlaç kaydı
    start_date = models.DateField()  # Programın başlangıç tarihi
    end_date = models.DateField(null=True, blank=True)  # (Opsiyonel) Bitiş tarihi
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, default='daily')
    interval = models.PositiveIntegerField(default=1)
    # 'custom' için kaç günde bir kullanılacağı (ör: interval=3 ise her 3 günde bir)
    days_of_week = models.ManyToManyField(WeekDay, blank=True)
    # Haftalık program için hangi günler (Çoktan-çoğa ilişki):contentReference[oaicite:5]{index=5}
    day_of_month = models.PositiveIntegerField(null=True, blank=True)
    # Aylık tekrar için ayın hangi günü alınacağı (1-31)
    doses_per_period = models.PositiveIntegerField(default=1)

    # Belirtilen periyotta kaç doz alınacağı (örneğin X günde Y kez)
    dose_amount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    dose_unit = models.CharField(max_length=50, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.medication.name} - {self.get_frequency_display()}"
