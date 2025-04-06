from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import WishlistAlbum, HouseFavorite
from .serializers import WishlistAlbumSerializer, HouseFavoriteSerializer
from .permissions import IsClientUserOrReadOnly
from .filters import WishlistFilters


class WishlistAlbumViewSet(viewsets.ModelViewSet):
    queryset = WishlistAlbum.objects.all()
    serializer_class = WishlistAlbumSerializer
    permission_classes = [ IsClientUserOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_class = WishlistFilters

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class HouseFavoriteViewSet(viewsets.ModelViewSet):
    queryset = HouseFavorite.objects.all()
    serializer_class = HouseFavoriteSerializer
    permission_classes = [IsAuthenticated, IsClientUserOrReadOnly]
