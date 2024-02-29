from rest_framework import generics

from customer.serializers import CustomerSerializer


class CreateCustomerView(generics.CreateAPIView):
    serializer_class = CustomerSerializer
