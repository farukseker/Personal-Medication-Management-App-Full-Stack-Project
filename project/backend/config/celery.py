from __future__ import absolute_import, unicode_literals
from config.settings.base import env
from celery import Celery, shared_task

# from asset.tasks import regular_asset_data_acquisition, regular_public_asset_data_acquisition


env('DJANGO_SETTINGS_MODULE')

app = Celery('config')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    return 2+5



from celery.schedules import crontab

app.conf.beat_schedule = {
    'daily-push-scheduler-every-minute': {
        'task': 'medication.tasks.medication_notification_task.notification_dispatcher',
        'schedule': crontab(minute='*'),  # her dakika
    },
}
