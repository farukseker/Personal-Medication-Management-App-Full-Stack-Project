from django.db import models
from django.contrib.auth import get_user_model
from datetime import time, datetime

User = get_user_model()


class NotificationSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    notifications_enabled = models.BooleanField(default=True)

    # --- NOTIFICATION_TYPES ---
    ALLOWED_NOTIFICATION_TYPES = {
        'medication': 'medication_enabled',
        'water': 'water_enabled',
        'weight': 'weight_enabled',
    }
    medication_enabled = models.BooleanField(default=True)
    water_enabled = models.BooleanField(default=True)
    weight_enabled = models.BooleanField(default=True)
    # --- NOTIFICATION_TYPES END ---

    use_time_range = models.BooleanField(default=False)
    start_time: time = models.TimeField(default=time(8, 0))   # 08:00
    end_time: time = models.TimeField(default=time(22, 0))    # 22:00

    def can_i_send_this_notification(self, notification_type) -> bool | None: # 'cause raise error
        if not self.notifications_enabled:
            return False

        now = datetime.now().time()
        if self.use_time_range and not (
                (self.start_time <= now <= self.end_time)
                if self.start_time < self.end_time
                else (now >= self.start_time or now <= self.end_time)
        ):
            return False

        try:
            return getattr(self, self.ALLOWED_NOTIFICATION_TYPES[notification_type])
        except KeyError:
            raise NotImplementedError(f'Unknown notification type: {notification_type}')
