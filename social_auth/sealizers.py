from rest_framework import serializers
from django.conf import settings

from social_auth import google, facebook

from social_auth.register import register_social_user


class GoogleSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate(self, auth_token: str) -> dict:
        """
        Validates the Google authentication token.

        :param auth_token: The authentication token to be validated.
        :return: A dictionary with information about the registered user

        raise: serializers.ValidationError: If the token is invalid, expired, or does not match.
        """
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


class FacebookSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token: str) -> dict:
        """
        Validates the Facebook authentication token.

        :param auth_token: The authentication token to be validated.
        :return: A dictionary with information about the registered user

        :raise: serializers.ValidationError: If the token is invalid or expired.
        """
        user_data = facebook.Facebook.validate(auth_token)
        try:
            email = user_data["email"]
            provider = "facebook"
            return register_social_user(provider=provider, email=email)
        except:
            raise serializers.ValidationError(
                "The token  is invalid or expired. Please login again."
            )
