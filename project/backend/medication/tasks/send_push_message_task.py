from celery import shared_task
from pywebpush import webpush, WebPushException
from medication.models import PushSubscription
from medication.utils.notifications import send_push



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
