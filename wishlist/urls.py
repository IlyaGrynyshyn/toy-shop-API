from rest_framework import routers
from wishlist.views import WishlistViewSet

app_name = "wishlist"
router = routers.DefaultRouter()
router.register("wishlist", WishlistViewSet, basename="wishlist")

urlpatterns = router.urls
