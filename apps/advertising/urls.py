from .views import AdvertisingAPI
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("advertising", AdvertisingAPI)

urlpatterns = router.urls
