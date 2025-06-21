from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db.models import CheckConstraint, Q

User = get_user_model()

class WeightEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="weight_entries")
    weight = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0.01)])  # 70.5 > 0.01
    date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'date']
        ordering = ['-date']
        constraints = [
            CheckConstraint(check=Q(weight__gt=0), name="weight_positive")
        ]

    def __str__(self):
        return f"{self.user} - {self.weight} kg on {self.date}"
