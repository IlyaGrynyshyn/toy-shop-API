from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from customer.serializers import CustomerSerializer, ChangePasswordSerializer


class CreateCustomerView(generics.CreateAPIView):
    """Create a new customer"""

    serializer_class = CustomerSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""

    serializer_class = CustomerSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class ChangePasswordViewSet(generics.UpdateAPIView):
    queryset = get_user_model()
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]
