from rest_framework import routers
from django.urls import path, include

from shop.views import ProductViewSet, CategoryViewSet, MaterialsViewSet

router = routers.DefaultRouter()
router.register("products", ProductViewSet, basename="product")
router.register("categories", CategoryViewSet, basename="category")
router.register("materials", MaterialsViewSet, basename="material")

urlpatterns = [path("", include(router.urls))]

app_name = "shop"
