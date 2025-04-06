from rest_framework.routers import DefaultRouter
from .views import HousingViewSet, ReviewViewSet, HousingReservationViewSet, RoomViewSet, \
    HousingAvailabilityViewSet, HousingImageSet

router = DefaultRouter()
router.register('housing', HousingViewSet)
router.register('housing_reservations', HousingReservationViewSet)
router.register('reviews', ReviewViewSet)
router.register('rooms', RoomViewSet)
router.register('availability', HousingAvailabilityViewSet)
router.register("housingimage", HousingImageSet)

urlpatterns = router.urls
