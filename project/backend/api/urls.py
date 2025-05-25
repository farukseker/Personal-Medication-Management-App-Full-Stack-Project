from django.urls import path, include

app_name = "api"

urlpatterns = [
    path('medication/', include('medication.api.urls'), name='medication'),
    path('counter/', include('counter.api.urls'), name='counter'),
    # path('medication/', include('medication_management.api.urls'), name='medication'),
    path('auth/', include('custom_auth.api.urls'), name='auth'),
]
