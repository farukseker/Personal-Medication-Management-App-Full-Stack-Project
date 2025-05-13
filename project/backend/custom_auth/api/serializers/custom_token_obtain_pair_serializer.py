from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        attrs = super().validate(attrs)
        return {
            "first_name": self.user.first_name,
            "email": self.user.email,
            # "permissions": self.user.user_permissions.values_list("codename", flat=True),
            # "groups": self.user.groups.values_list("name", flat=True),
            **attrs,
        }
