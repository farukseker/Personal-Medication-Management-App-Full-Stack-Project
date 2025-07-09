from celery import shared_task


@shared_task
def notification_dispatcher():
    from notification_base.tasks.send_push_message_task import send_push_notification_message
    from datetime import datetime, timedelta
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

                key = f"notif:{schedule.id}:{dose_time.time}:{today}"
                if cache.get(key):
                    continue
                cache.set(key, True, timeout=3600)

                pyload: dict[str, str] = {
                    "title": "İlaç Hatırlatıcı",
                    "body": f"{schedule.medication.name} ilacını alma zamanı ({dose_time.time.strftime('%H:%M')})"
                }
                send_push_notification_message.delay(user.id, pyload)
