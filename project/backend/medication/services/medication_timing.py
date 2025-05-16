from datetime import date
from django.utils.timezone import localdate
from medication.models import MedicationSchedule, MedicationDoseTime, MedicationLog

class MedicationTimeService:
    @staticmethod
    def for_user_today(user):
        today = localdate()
        return MedicationTimeService.for_user_on_date(user, today)

    @staticmethod
    def for_user_on_date(user, target_date: date):
        schedules = MedicationSchedule.objects.filter(
            medication__user=user,
            start_date__lte=target_date
        ).select_related('medication')

        taken_logs = MedicationLog.objects.filter(user=user, date=target_date)
        taken_map = {
            (
                log.medication_id,
                log.time,
                log.dose_time_id
            )
            for log in taken_logs if log.time is not None
        }

        taken_dose_time_ids = {
            log.dose_time_id
            for log in taken_logs
            if log.time is not None and log.dose_time_id is not None
        }

        due_medications = []

        for schedule in schedules:
            if schedule.end_date and schedule.end_date < target_date:
                continue

            if not MedicationTimeService.is_due_on(schedule, target_date):
                continue

            for dose_time in schedule.medication.dose_times.all():
                dose_time_key = (schedule.medication.id, dose_time.time)

                if dose_time.id in taken_dose_time_ids:
                    continue

                if dose_time_key in taken_map:
                    continue

                due_medications.append({
                    'medication_name': schedule.medication.name,
                    'dose': dose_time.dose_amount or schedule.dose_amount,
                    'unit': dose_time.dose_unit or schedule.dose_unit,
                    'dose_time_id': dose_time.id,
                    # 'schedules': schedule.id,
                    'schedule_id': schedule.id,
                    'medication_id': schedule.medication.id,
                    'time': dose_time.time.strftime('%H:%M'),
                })

        return due_medications

    @staticmethod
    def is_due_on(schedule, target_date: date):
        frequency = schedule.frequency
        interval = schedule.interval
        start = schedule.start_date
        delta_days = (target_date - start).days

        if delta_days < 0:
            return False

        if frequency == 'daily':
            return delta_days % interval == 0

        elif frequency == 'weekly':
            weekday_name = target_date.strftime('%A')
            weekdays = schedule.days_of_week.values_list('name', flat=True)
            return weekday_name in weekdays and (delta_days // 7) % interval == 0

        elif frequency == 'monthly':
            return target_date.day == schedule.day_of_month

        elif frequency == 'custom':
            return delta_days % interval == 0

        return False
