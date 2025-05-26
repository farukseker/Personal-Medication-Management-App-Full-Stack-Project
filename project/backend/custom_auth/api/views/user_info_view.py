from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from counter.api.serializers import UserInfoSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class UserInfoView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserInfoSerializer


    def get(self, request, *args, **kwargs):
        return Response(
            UserInfoSerializer(instance=self.request.user).data,
            status=200
        )
