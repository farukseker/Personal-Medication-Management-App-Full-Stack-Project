from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class WaterGoal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="water_goal")
    daily_goal = models.PositiveIntegerField(default=2000)  # ml cinsinden

    def __str__(self):
        return f"{self.user.username} - {self.daily_goal} ml"


class WaterEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="water_entries")
    amount = models.PositiveIntegerField()  # ml
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount} ml at {self.timestamp}"
