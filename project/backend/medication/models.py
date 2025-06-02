from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class WeekDay(models.Model):
    """Haftanın günü modelidir (Pazartesi, Salı vb.)."""
    name = models.CharField(max_length=10, unique=True)  # Örneğin 'Pazartesi', 'Salı'
    WEEKDAY_CHOICES = [
        ('monday', 'Pazartesi'),
        ('tuesday', 'Sal'),
        ('wednesday', 'Çarşamba'),
        ('thursday', 'Perşembe'),
        ('friday', 'Cuma'),
        ('saturday', 'Cumartesi'),
        ('sunday', 'Pazar')
    ]

    def __str__(self):
        return self.name


class Medication(models.Model):
    """Bir kullanıcının eklediği ilaç kaydı."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # İlaç kaydının sahibi kullanıcı
    name = models.CharField(max_length=200)  # İlaç adı
    is_active = models.BooleanField(default=True)  # Aktif olup olmadığı (silindiğinde False yapılır)
    default_dose_amount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        null=True,
        blank=True
    )  # Varsayılan doz miktarı
    default_dose_unit = models.CharField(max_length=50, blank=True)  # Doz birimi (örn. 'mg', 'tablet')
    created_at = models.DateTimeField(auto_now_add=True)  # Oluşturulma zamanı
    updated_at = models.DateTimeField(auto_now=True)  # Güncellenme zamanı

    def __str__(self):
        return f"{self.name} ({self.user.username})"


class MedicationSchedule(models.Model):
    """İlacın tekrar eden kullanım planını tutar."""
    FREQUENCY_CHOICES = [
        ('daily', 'Günlük'),
        ('weekly', 'Haftalık'),
        ('monthly', 'Aylık'),
        ('custom', 'Özel'),
    ]
    medication = models.ForeignKey(Medication, on_delete=models.CASCADE, related_name='schedules')  # İlaç kaydı
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
    # Doz miktarı ve birimi, doz değişimleri için farklı kayıtlar oluşturulabilir
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.medication.name} - {self.get_frequency_display()}"

class MedicationDoseTime(models.Model):
    # Her doz zamanı için kayıt (örn. sabah 08:00'de 1 tablet)
    schedule = models.ForeignKey(MedicationSchedule, on_delete=models.CASCADE, related_name='dose_times')
    time = models.TimeField()           # Örneğin sabah 08:00
    dose_amount = models.FloatField()  # Örneğin 1.0
    dose_unit = models.CharField(max_length=20)  # Örneğin 'tablet'

    class Meta:
        unique_together = ('schedule', 'time')  # Aynı programda aynı saati tekrar girilmesin

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
    medication = models.ForeignKey(Medication, null=True, blank=True, on_delete=models.SET_NULL)
    dose_time = models.ForeignKey(MedicationDoseTime, null=True, blank=True, on_delete=models.SET_NULL)

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


class DailyNote(models.Model):
    """Kullanıcının belirli bir gün için eklediği not."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Notu ekleyen kullanıcı
    date = models.DateField()  # Not tarihi
    note = models.TextField()  # Not içeriği
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'date')  # Her kullanıcı + tarihe göre tekil olabilir

    def __str__(self):
        return f"Note for {self.user.username} on {self.date}"


class MedicationAutoCompilationModel(models.Model):
    name = models.CharField(max_length=255)
    barcode = models.CharField(max_length=30, blank=True)
    value = models.CharField(max_length=30, blank=True)
    unit = models.CharField(max_length=30, blank=True)


class MedicationStock(models.Model):
    """İlaç stok takibini sağlar."""
    medication = models.OneToOneField(Medication, on_delete=models.CASCADE, related_name='stock')
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

class PushSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    endpoint = models.TextField()
    p256dh = models.CharField(max_length=255)
    auth = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
