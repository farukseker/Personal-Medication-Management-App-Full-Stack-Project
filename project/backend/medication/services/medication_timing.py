from datetime import timedelta, date
from medication.models import MedicationSchedule, WeekDay
from django.utils.timezone import localdate, now


class MedicationTimeService:
    @staticmethod
    def for_user_today(user):
        today = localdate(now())
        return MedicationTimeService.for_user_on_date(user, today)

    @staticmethod
    def for_user_on_date(user, target_date: date):
        schedules = MedicationSchedule.objects.filter(
            medication__user=user,
            start_date__lte=target_date
        ).select_related('medication')

        due_medications = []

        for schedule in schedules:
            if schedule.end_date and schedule.end_date < target_date:
                continue  # program bitmiş

            if MedicationTimeService.is_due_on(schedule, target_date):
                # schedule
                due_medications.append({
                    'medication_name': schedule.medication.name,
                    'dose': schedule.dose_amount,
                    'unit': schedule.dose_unit,
                    'schedules_id': schedule.id,
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
