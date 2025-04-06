from rest_framework.routers import DefaultRouter
from .views import HouseFavoriteViewSet, WishlistAlbumViewSet

router = DefaultRouter()
router.register('wishlist', WishlistAlbumViewSet)
router.register('favorites', HouseFavoriteViewSet)

urlpatterns = router.urls
