from rest_framework import routers
from django.urls import path, include

from shop.views import ProductViewSet

router = routers.DefaultRouter()
router.register("product", ProductViewSet, basename="product")

urlpatterns = [path("", include(router.urls))]

app_name = "shop"
