from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from notification_base.models import PushSubscription
from medication.utils.notifications import send_push


class SendNotificationView(APIView):
    def post(self, request):
        payload = request.data.get("payload", {"title": "Merhaba", "body": "Test bildirimi"})
        errors = []

        for sub in PushSubscription.objects.all():
            success, error = send_push(sub.subscription_info, payload)
            if not success:
                errors.append({"endpoint": sub.endpoint, "error": error})
        if errors:
            return Response({"message": "Bazı bildirimler gönderilemedi", "errors": errors}, status=207)

        return Response({"message": "Tüm bildirimler gönderildi"}, status=200)
