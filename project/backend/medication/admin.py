from django.contrib import admin
from .models import *


admin.site.register(WeekDay)
admin.site.register(Medication)
admin.site.register(MedicationSchedule)
admin.site.register(MedicationLog)
admin.site.register(DailyNote)
admin.site.register(MedicationDoseTime)
admin.site.register(PushSubscription)
