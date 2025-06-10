from celery import shared_task
from django.utils.timezone import localdate


@shared_task
def notification_dispatcher():
    from datetime import timezone, datetime, timedelta
    from django.db.models import Q
    from medication.models import MedicationSchedule
    from medication.services import MedicationTimeService
    from django.core.cache import cache


    now = datetime.now()
    today = now.date()
    current_time = now.time().replace(second=0, microsecond=0)
    print(f'ON WORK: {current_time}')

    # tolerans: +-1 dk
    lower = (datetime.combine(today, current_time) - timedelta(minutes=1)).time()
    upper = (datetime.combine(today, current_time) + timedelta(minutes=1)).time()

    schedules = MedicationSchedule.objects.filter(
        start_date__lte=today,
    ).filter(
        Q(end_date__isnull=True) | Q(end_date__gte=today)
    ).select_related('medication', 'medication__user').prefetch_related('dose_times')

    for schedule in schedules:
        if not MedicationTimeService.is_due_on(schedule, today):
            continue

        for dose_time in schedule.dose_times.all():
            if lower <= dose_time.time <= upper:
                user = schedule.medication.user
                message = f"{schedule.medication.name} ilacını alma zamanı ({dose_time.time.strftime('%H:%M')})"
                print(message)

                key = f"notif:{schedule.id}:{dose_time.time}:{today}"
                if cache.get(key):
                    continue
                cache.set(key, True, timeout=3600)  # 1 saat sonra silinir

                # send_push_notification.delay(user.id, message)

from celery import shared_task
from pywebpush import webpush, WebPushException
from medication.models import PushSubscription
from django.conf import settings

# VAPID_PRIVATE_KEY = 'YKZe-OOtQijtK4KVMiFooViNgUfa7-AKC9N2Yglkm1Q'
VAPID_PRIVATE_KEY = 'CuTHAvMQvjmY3fMYaIBZs17AphdNH18NXFLmnZh7QIE'
VAPID_CLAIMS = {
    "sub": "mailto:your-email@example.com"
}

@shared_task
def send_push_message(subscription_id, payload):
    print('push side:')
    try:
        sub = PushSubscription.objects.get(id=subscription_id)
        webpush(
            subscription_info={
                "endpoint": sub.endpoint,
                "keys": {
                    "p256dh": sub.p256dh,
                    "auth": sub.auth,
                },
            },
            data=payload,
            vapid_private_key=VAPID_PRIVATE_KEY,
            vapid_claims=VAPID_CLAIMS,
        )
    except PushSubscription.DoesNotExist:
        print(f"Subscription {subscription_id} bulunamadı.")
    except WebPushException as ex:
        print(f"Push gönderilemedi: {repr(ex)}")
