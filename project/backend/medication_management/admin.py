from django.contrib import admin
from medication_management.models import MedicationModel, MedicationUseHistoryModel, StageSteps, MedicationReminderModel


admin.site.register(MedicationModel)
admin.site.register(StageSteps)
admin.site.register(MedicationUseHistoryModel)
admin.site.register(MedicationReminderModel)
