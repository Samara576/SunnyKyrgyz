from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .paginations import StandardResultsSetPagination, TravelLimitOffsetPagination
from .permissions import IsOwnerUserOrReadOnly, IsClientUserOrReadOnly
from .models import HousingReview, HousingReservation, Housing, Room, HousingAvailability, \
    HousingImage
from .serializers import HousingReviewSerializer, HousingReservationSerializer, RoomGetSerializer, \
    RoomPostSerializer, HousingGetSerializer, HousingPostSerializer, \
    HousingAvailabilityPostSerializer, HousingImageSerializer, HousingAvailabilityGetSerializer
from .filters import HousingFilter, RoomFilter
from .utils import retrieve_currency, CurrencyParaMixin, perform_create


class HousingViewSet(viewsets.ModelViewSet):
    queryset = Housing.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = HousingFilter
    permission_classes = [IsOwnerUserOrReadOnly]
    pagination_class = TravelLimitOffsetPagination
    ordering_fields = ['stars']
    serializer_class = HousingPostSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return HousingGetSerializer
        return self.serializer_class

    @action(detail=True, methods=['POST'])
    def add_to_favorite(self, request, pk=None):
        instance = self.get_object()
        instance.is_favorite = True
        instance.save()
        return Response('Объект успешно добавлен в избранное!')

    # def retrieve(self, request, *args, **kwargs):
    #     return retrieve_housetrans(self, request, *args, **kwargs)


class HousingReservationViewSet(viewsets.ModelViewSet):
    queryset = HousingReservation.objects.all()
    serializer_class = HousingReservationSerializer
    permission_classes = [IsClientUserOrReadOnly]

    def perform_create(self, serializer, *args, **kwargs):
        return perform_create(self, serializer)

    # def retrieve(self, request, *args, **kwargs):
    #     return retrieve_reservationtrans(self, request, *args, **kwargs)


class HousingAvailabilityViewSet(viewsets.ModelViewSet):
    queryset = HousingAvailability.objects.all()
    serializer_class = HousingAvailabilityPostSerializer
    permission_classes = [IsOwnerUserOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return HousingAvailabilityGetSerializer
        return self.serializer_class


class RoomViewSet(viewsets.ModelViewSet, CurrencyParaMixin):
    queryset = Room.objects.all()
    permission_classes = [IsOwnerUserOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = RoomFilter
    ordering_fields = ['price_per_night']
    pagination_class = StandardResultsSetPagination
    serializer_class = RoomPostSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RoomGetSerializer
        return self.serializer_class

    def retrieve(self, request, *args, **kwargs):
        return retrieve_currency(self, request, *args, **kwargs)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = HousingReview.objects.all()
    serializer_class = HousingReviewSerializer
    permission_classes = [IsClientUserOrReadOnly]


class HousingImageSet(viewsets.ModelViewSet):
    queryset = HousingImage.objects.all()
    serializer_class = HousingImageSerializer
    permission_classes = [IsOwnerUserOrReadOnly]
