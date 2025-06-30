from django.urls import path
from notification_base.api.views import NotificationSettingsDetailUpdateView, SubscribeView


urlpatterns = [
    path('settings/', NotificationSettingsDetailUpdateView.as_view(), name='notification-settings'),
    path('subscribe/', SubscribeView.as_view()),
    # unsubscribe
    # unsubscribe/all/ > settings | when
]
