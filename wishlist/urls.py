from rest_framework import routers
from wishlist.views import WishlistViewSet

router = routers.DefaultRouter()
router.register("wishlist", WishlistViewSet, basename="wishlist")

urlpatterns = router.urls
