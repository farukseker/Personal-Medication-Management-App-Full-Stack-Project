from django.db import models


class CounterModel(models.Model):
    name = models.CharField()
    COUNTER_CHOICES = [
        ('daily', 'Günlük'),
        ('weekly', 'Haftalık'),
        ('monthly', 'Aylık'),
        ('unlimited', 'Sınırsız'),
    ]
    counter_type = models.CharField(max_length=10, choices=COUNTER_CHOICES, default='daily')
    can_average = models.BooleanField(default=False)


class CounterTickModel(models.Model):
    counter_ref = models.ForeignKey(CounterModel, on_delete=models.CASCADE, related_name=' counter_tick')
    created_at = models.DateTimeField(auto_now_add=True)
    tick = models.IntegerField()
