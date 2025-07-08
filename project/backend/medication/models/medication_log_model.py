from django.db import models
from django.contrib.auth import get_user_model
from .medication_stock_model import MedicationStock

User = get_user_model()


class MedicationLog(models.Model):
    """
    sechglude id koy böylece hangi durumun ilacı alındı anlarız time sync e gerek yok aynı mantık da olur
    second:
    """
    TAKEN_CHOICES = [
        ('be_taken', 'Alınacak'),
        ('taken', 'Aldındı'),
        ('pass', 'Pas'),
    ]
    """Kullanıcının bir ilacı aldığı zamanı kaydeder (geçmiş kayıtlar)."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Kayıt sahibi kullanıcı
    medication = models.ForeignKey('medication.Medication', null=True, blank=True, on_delete=models.SET_NULL)
    dose_time = models.ForeignKey('medication.MedicationDoseTime', null=True, blank=True, on_delete=models.SET_NULL)

    # Ilacın FK'sı, silinirse null olur
    medication_name = models.CharField(max_length=200)
    # Kayıt sırasında ilaç adı (silinen ilaç için gösterim)
    date = models.DateField()  # Alım tarihi
    time = models.TimeField(null=True, blank=True)
    # Alım saati (opsiyonel)
    taken_time = models.TimeField(null=True, blank=True)
    taken_status = models.CharField(max_length=10, choices=TAKEN_CHOICES, default='be_taken')

    dose_taken = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    dose_unit = models.CharField(max_length=50, blank=True)
    # Alınan doz miktarı ve birimi
    notes = models.TextField(blank=True)  # Alımla ilgili isteğe bağlı notlar

    class Meta:
        ordering = ['-date', '-time']

    def __str__(self):
        return f"{self.medication_name} on {self.date}"

    def save(self, *args, **kwargs):
        is_new = self.pk is None  # Yeni kayıt mı kontrolü

        super().save(*args, **kwargs)  # Önce kaydediyoruz ki ID oluşsun

        if is_new and self.taken_status == 'taken' and self.medication and self.dose_taken:
            try:
                stock = self.medication.stock
                stock.quantity = max(stock.quantity - self.dose_taken, 0)
                stock.save()
            except MedicationStock.DoesNotExist:
                pass  # Stok bilgisi yoksa sessizce geç

