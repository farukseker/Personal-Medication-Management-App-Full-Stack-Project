from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from medication.models import PushSubscription
from medication.utils.notifications import send_push


class SendNotificationView(APIView):
    def post(self, request):
        payload = request.data.get("payload", {"title": "Merhaba", "body": "Test bildirimi"})
        errors = []

        for sub in PushSubscription.objects.all():
            subscription_info = {
                "endpoint": sub.endpoint,
                "keys": {
                    "p256dh": sub.p256dh,
                    "auth": sub.auth,
                }
            }
            success, error = send_push(subscription_info, payload)
            if not success:
                errors.append({"endpoint": sub.endpoint, "error": error})

        if errors:
            return Response({"message": "Bazı bildirimler gönderilemedi", "errors": errors}, status=207)

        return Response({"message": "Tüm bildirimler gönderildi"}, status=200)
