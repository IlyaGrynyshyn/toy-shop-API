from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from customer.serializers import CustomerSerializer

USER_DATA = {
    "email": "test@test.com",
    "password": "qwerty123",
    "first_name": "Bob",
    "last_name": "May",
}


class CustomerSerializerTests(APITestCase):
    def test_valid_serializer_data(self):
        user_data = USER_DATA
        serializer = CustomerSerializer(data=user_data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_serializer_data(self):
        user_data = {}
        serializer = CustomerSerializer(data=user_data)
        self.assertFalse(serializer.is_valid())
        self.assertTrue("email" in serializer.errors)
        self.assertTrue("password" in serializer.errors)

    def test_create_user(self):
        user_data = USER_DATA
        serializer = CustomerSerializer(data=user_data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertIsInstance(user, get_user_model())
        self.assertEqual(user.email, user_data["email"])

    def test_update_user_password(self):
        user = get_user_model().objects.create_user(
            email=USER_DATA["email"],
            password=USER_DATA["password"],
            first_name=USER_DATA["first_name"],
            last_name=USER_DATA["last_name"],
        )
        new_password = "newpassword"
        update_data = {"password": new_password}
        serializer = CustomerSerializer(instance=user, data=update_data, partial=True)
        self.assertTrue(serializer.is_valid())
        updated_user = serializer.save()
        self.assertTrue(updated_user.check_password(new_password))
