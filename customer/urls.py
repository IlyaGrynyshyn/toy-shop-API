from django.urls import path
from customer.views import CreateCustomerView


app_name: str = "customer"
urlpatterns = [
    path("registration/", CreateCustomerView.as_view(), name="create"),
]
