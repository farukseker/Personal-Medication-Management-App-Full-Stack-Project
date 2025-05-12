from django.urls import path, include

app_name = "api"

urlpatterns = [
    path('medication/', include('medication_management.api.urls'), name='medication')
]
