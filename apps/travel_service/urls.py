from rest_framework.routers import DefaultRouter
from .views import TransferViewSet, TransferReservationViewSet, ReviewViewSet

router = DefaultRouter()
router.register('transfers', TransferViewSet)
router.register('transfer_reservations', TransferReservationViewSet)
router.register('transfer_reviews', ReviewViewSet)
urlpatterns = router.urls
