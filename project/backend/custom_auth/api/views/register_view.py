from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_406_NOT_ACCEPTABLE
from custom_auth.api.serializers import UserRegisterSerializer
from custom_auth.models import User


class RegisterView(APIView):
    serializer_class = UserRegisterSerializer

    def post(self, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid() and not User.objects.filter(email=serializer.validated_data.get('email')).exists():
            User.objects.create_user(**serializer.validated_data)
            return Response([], status=HTTP_201_CREATED)
        return Response([], status=HTTP_406_NOT_ACCEPTABLE)
