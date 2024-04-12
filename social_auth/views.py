from rest_framework import generics, status
from rest_framework.response import Response

from social_auth.sealizers import (
    GoogleSocialAuthSerializer,
    FacebookSocialAuthSerializer,
)


class GoogleSocialAuthView(generics.GenericAPIView):
    serializer_class = GoogleSocialAuthSerializer

    def post(self, request, *args, **kwargs) -> Response:
        """
        Send an idtoken as from google to get user information.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = (serializer.validated_data)["auth_token"]
        return Response(data, status=status.HTTP_200_OK)


class FacebookSocialAuthView(generics.GenericAPIView):
    serializer_class = FacebookSocialAuthSerializer

    def post(self, request, *args, **kwargs) -> Response:
        """
        Send an access token as from facebook to get user information.
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = (serializer.validated_data)["auth_token"]
        return Response(data, status=status.HTTP_200_OK)
