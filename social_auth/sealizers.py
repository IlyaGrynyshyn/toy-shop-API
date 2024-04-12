from rest_framework import serializers
from django.conf import settings

from social_auth import google

from social_auth.register import register_social_user


class GoogleSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate(self, auth_token):
        user_data = google.Google.validate(auth_token)
        try:
            user_data["sub"]
        except:
            raise serializers.ValidationError(
                "The token is invalid or expired. Please try again."
            )
        if user_data["sub"] != settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY:
            raise serializers.ValidationError("oops, Who are you?")

        email = user_data["email"]
        provider = "google"

        return register_social_user(provider=provider, email=email)
