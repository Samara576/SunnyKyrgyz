from rest_framework.viewsets import ModelViewSet
from .models import Advertising
from .permissions import IsAdminUserOrReadOnly
from .serializers import AdvertisingSerializer


class AdvertisingAPI(ModelViewSet):
    queryset = Advertising.objects.all()
    serializer_class = AdvertisingSerializer
    permission_classes = [IsAdminUserOrReadOnly]
