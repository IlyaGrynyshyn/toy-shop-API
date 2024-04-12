from django.urls import path
from customer.views import CreateCustomerView, ManageUserView, ChangePasswordViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


app_name: str = "customer"
urlpatterns = [
    path("registration/", CreateCustomerView.as_view(), name="create"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("me/", ManageUserView.as_view(), name="manage"),
    path(
        "change_password/<int:pk>/",
        ChangePasswordViewSet.as_view(),
        name="change_password",
    ),
]
