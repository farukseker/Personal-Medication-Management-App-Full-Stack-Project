from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class PushSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    endpoint = models.TextField()
    p256dh = models.CharField(max_length=255)
    auth = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def subscription_info(self) -> dict:
        return {
                "endpoint": self.endpoint,
                "keys": {
                    "p256dh": self.p256dh,
                    "auth": self.auth,
                }
            }
