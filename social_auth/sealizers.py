import os

from rest_framework import serializers
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed

from social_auth import google, facebook

from social_auth.register import register_social_user


class GoogleSocialAuthSerializer(serializers.Serializer):
    auth_token = serializers.CharField()

    def validate_auth_token(self, auth_token):
        user_data = google.Google.validate(auth_token)
        print(user_data)
        try:
            user_data["sub"]
        except:
            raise serializers.ValidationError(
                "The token is invalid or expired. Please login again."
            )

        if user_data["aud"] != os.environ.get("GOOGLE_CLIENT_ID"):

            raise AuthenticationFailed("oops, who are you?")

        email = user_data["email"]
        first_name = user_data["given_name"]
        last_name = user_data["family_name"]
        provider = "google"

        return register_social_user(
            provider=provider, email=email, first_name=first_name, last_name=last_name
        )


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
