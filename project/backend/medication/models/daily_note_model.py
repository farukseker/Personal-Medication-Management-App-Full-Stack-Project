from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


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
