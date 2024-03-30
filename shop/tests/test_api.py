from pathlib import Path

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken

from customer.models import Customer
from shop.models import Category, Product, Material

CATEGORIES_LIST_URL = reverse("shop:category-list")
PRODUCTS_LIST_URL = reverse("shop:product-list")


class CategoryAPITestCase(APITestCase):
    def setUp(self):
        self.url = CATEGORIES_LIST_URL
        self.validated_data = {"title": "Test Category", "slug": "test-category"}
        self.admin_user = Customer.objects.create(
            email="test@test.com", password="qwerty123", is_staff=True
        )
        self.customer_user = Customer.objects.create(
            email="customer_user", password="qwerty123", is_staff=False
        )
        self.admin_access_token = AccessToken.for_user(self.admin_user)
        self.customer_access_token = AccessToken.for_user(self.customer_user)

    def api_authentication_with_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.admin_access_token}")

    def api_authentication_with_customer(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.customer_access_token}"
        )

    def test_get_categories(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_category_with_admin_user(self):
        self.api_authentication_with_admin()
        response = self.client.post(self.url, self.validated_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_category_with_customer_user(self):
        self.api_authentication_with_customer()
        response = self.client.post(self.url, self.validated_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ProductAPITestCase(APITestCase):
    def setUp(self):
        self.url = PRODUCTS_LIST_URL
        self.category = Category.objects.create(
            title="Test Category", slug="test-category"
        )
        self.material = Material.objects.create(name="Test Material")
        self.product_1 = Product.objects.create(
            title="Test Product 1",
            slug="test-product-1",
            category=self.category,
            price=10,
            size=30,
        )
        self.product_2 = Product.objects.create(
            title="Test Product 2",
            slug="test-product-2",
            category=self.category,
            price=20,
            size=30,
        )
        self.product_3 = Product.objects.create(
            title="Test Product 3",
            slug="test-product-3",
            category=self.category,
            price=30,
            size=30,
        )
        self.test_image_path = (
            Path(__file__).resolve().parent.parent / "tests/test_image.jpg"
        )
        self.admin_user = Customer.objects.create(
            email="test@test.com", password="qwerty123", is_staff=True
        )
        self.customer_user = Customer.objects.create(
            email="customer_user", password="qwerty123", is_staff=False
        )
        self.invalid_data = {}
        self.admin_access_token = AccessToken.for_user(self.admin_user)
        self.customer_access_token = AccessToken.for_user(self.customer_user)

    def api_authentication_with_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.admin_access_token}")

    def api_authentication_with_customer(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {self.customer_access_token}"
        )

    def test_get_products(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_add_product_with_admin_user_with_valid_data(self):
        with open(self.test_image_path, "rb") as image_file:
            self.product_data = {
                "title": "Test Product",
                "category": self.category.pk,
                "slug": "test-product",
                "price": 100,
                "size": 10,
                "description": "bobob",
                "uploaded_images": [image_file],
            }
            self.api_authentication_with_admin()
            response = self.client.post(self.url, self.product_data)
            print(response.data)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_product_with_admin_user_invalid_data(self):
        self.api_authentication_with_admin()
        response = self.client.post(self.url, self.invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_product_with_customer_user(self):
        self.api_authentication_with_customer()
        response = self.client.post(self.url, self.invalid_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_filter_products_by_price_ASC(self):
        response = self.client.get(self.url, {"sort": "price_asc"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["price"], 10)
        self.assertEqual(response.data[1]["price"], 20)
        self.assertEqual(response.data[2]["price"], 30)

    def test_filter_products_by_price_DESC(self):
        response = self.client.get(self.url, {"sort": "price_desc"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["price"], 30)
        self.assertEqual(response.data[1]["price"], 20)
        self.assertEqual(response.data[2]["price"], 10)
