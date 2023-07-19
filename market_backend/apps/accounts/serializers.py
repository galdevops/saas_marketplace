from .models import User
from djoser.conf import settings
from djoser.serializers import TokenCreateSerializer, UserSerializer
from rest_framework.exceptions import ValidationError
from django.contrib.auth import authenticate, get_user_model


User = get_user_model()

# \Lib\site-packages\djoser\serializers.py
# class CustomActivationSerializer(ActivationSerializer):
#     default_error_messages = {
#         "stale_token": settings.CONSTANTS.messages.STALE_TOKEN_ERROR
#     }

#     def validate(self, attrs):
#         attrs = super().validate(attrs)
#         if not self.user.is_active:
#             return attrs
#         raise exceptions.PermissionDenied(self.error_messages["stale_token"])




class UserCustomSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        fields = ("email", "first_name")



class CustomTokenCreateSerializer(TokenCreateSerializer):

    def validate(self, attrs):
        password = attrs.get("password")
        params = {settings.LOGIN_FIELD: attrs.get(settings.LOGIN_FIELD)}
        self.user = authenticate(
            request=self.context.get("request"), **params, password=password
        )
        if not self.user:
            self.user = User.objects.filter(**params).first()
            if self.user and not self.user.check_password(password):
                self.fail("invalid_credentials")
            if not self.user.is_active:
                raise ValidationError("Please activate your account.")

        if self.user:
            return attrs
        self.fail("invalid_credentials")