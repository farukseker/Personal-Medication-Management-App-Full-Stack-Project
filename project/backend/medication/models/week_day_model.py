from django.db import models


class WeekDay(models.Model):
    name = models.CharField(max_length=10, unique=True)
    WEEKDAY_CHOICES: list[dict] = [
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
