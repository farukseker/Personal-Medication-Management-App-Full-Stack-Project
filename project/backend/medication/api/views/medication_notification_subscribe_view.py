from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from medication.models import PushSubscription


class SubscribeView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            PushSubscription.objects.create(
                endpoint=data['endpoint'],
                p256dh=data['keys']['p256dh'],
                auth=data['keys']['auth'],
                user=request.user if request.user.is_authenticated else None
            )
            return Response({"message": "Subscribed"}, status=status.HTTP_201_CREATED)
        except KeyError:
            return Response({"error": "Eksik alan"}, status=status.HTTP_400_BAD_REQUEST)
