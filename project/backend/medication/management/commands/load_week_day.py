from django.core.management.base import BaseCommand, CommandError
from medication.models import WeekDay
from django.core.exceptions import ValidationError


class Command(BaseCommand):
    def add_arguments(self, parser):
        ...

    @staticmethod
    def bulk_update_medications(day_list: list[str]):
        if WeekDay.objects.count() >= 6:
            raise ValidationError('Days are already defined')

        WeekDay.objects.bulk_create([
            WeekDay(**{
                "id": index,
                "name": day
            })
            for index, day in enumerate(day_list)
        ])

    def handle(self, *args, **options):
        day_list = [
            'monday',
            'tuesday',
            'wednesday',
            'thursday',
            'friday',
            'saturday',
            'sunday',
        ]
        self.bulk_update_medications(day_list)
