from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from customer.models import Customer

CUSTOMER_CREATE_URL = reverse("customer:create")
MANAGE_CUSTOMER_URL = reverse("customer:manage")


class CreateCustomerViewTests(APITestCase):
    def test_create_customer(self):
        url = CUSTOMER_CREATE_URL
        data = {
            "email": "test@example.com",
            "password": "testpassword",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue("id" in response.data)

    def test_create_customer_invalid_data(self):
        url = CUSTOMER_CREATE_URL
        data = {}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ManageUserViewTests(APITestCase):
    def setUp(self):
        self.customer = Customer.objects.create(
            email="test@test.com",
            password="qwerty123",
        )
        self.access_token = AccessToken.for_user(self.customer)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.access_token}")

    def test_get_authenticated_user(self):
        url = MANAGE_CUSTOMER_URL
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["email"], self.customer.email)

    def test_get_authenticated_user_unauthorized(self):
        self.client.credentials()
        url = MANAGE_CUSTOMER_URL
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
