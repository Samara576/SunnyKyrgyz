from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.travel.urls import router as travel_router
# from apps.news.urls import router as news_router
from apps.travel.views import HousingViewSet
from apps.travel_service.urls import router as travel_service_router
# from apps.weather_forecast.urls import router as weather_router
from apps.users.urls import router as users_router
from apps.advertising.urls import router as advertising_router
from .settings.yasg import urlpatterns_swagger as doc_urls

routers = [
    travel_router,
    travel_service_router,
    users_router,
    advertising_router,
]

router = DefaultRouter()
for rtr in routers:
    router.registry.extend(rtr.registry)

urlpatterns = [
      path('admin/', admin.site.urls),
      path('api/users/', include('apps.users.urls')),
      path('api/favorite/', include('apps.favorite.urls')),
      path('housing/<int:pk>/availability/', HousingViewSet.as_view({'get': 'availability'})),
          ] + router.urls + doc_urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
