# Generated by Django 5.2.1 on 2025-06-27 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medication', '0003_medicationstock_pushsubscription'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PushSubscription',
        ),
    ]
