from celery import shared_task
from notification_base.models import PushSubscription
from pywebpush import webpush, WebPushException
import json


# https://chatgpt.com/share/685e266d-e4b8-8009-b229-f68788a04ac8 |
# yük artışı için bir not                                        |


def send_push(subscription_info, payload):
    from config.settings.base import VAPID_EMAIL, VAPID_PRIVATE_KEY

    try:
        webpush(
            subscription_info=subscription_info,
            data=json.dumps(payload),
            vapid_private_key=VAPID_PRIVATE_KEY,
            vapid_claims={"sub": VAPID_EMAIL}
        )
        return True, None
    except WebPushException as e:
        return False, str(e)


@shared_task
def send_push_notification_message(subscription_user_id: int, payload: str) -> None:
    errors: list[dict] = []
    try:
        for sub in PushSubscription.objects.filter(user_id=subscription_user_id):
            success, error = send_push(sub.subscription_info, payload)
            if not success:
                errors.append({"endpoint": sub.endpoint, "error": error})
    except PushSubscription.DoesNotExist:
        print(f"Subscription ({subscription_user_id}) bulunamadı.")
    except WebPushException as ex:
        print(f"Push gönderilemedi: {repr(ex)}")
