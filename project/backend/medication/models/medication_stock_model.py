from django.db import models


class MedicationStock(models.Model):
    """İlaç stok takibini sağlar."""
    medication = models.OneToOneField('medication.Medication', on_delete=models.CASCADE, related_name='stock')
    quantity = models.DecimalField(max_digits=7, decimal_places=2, default=0)  # Mevcut stok miktarı
    unit = models.CharField(max_length=50)  # 'tablet', 'ml' vs.
    min_threshold = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    # Uyarı için minimum stok seviyesi
    last_updated = models.DateTimeField(auto_now=True)

    def is_below_threshold(self):
        if self.min_threshold is not None:
            return self.quantity < self.min_threshold
        return False

    def __str__(self):
        return f"{self.medication.name} - {self.quantity} {self.unit}"
