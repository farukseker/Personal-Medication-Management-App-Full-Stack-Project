# Generated by Django 5.2.1 on 2025-06-23 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_monitoring', '0002_alter_weightentry_weight_weightentry_weight_positive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weightentry',
            name='date',
            field=models.DateField(),
        ),
    ]
