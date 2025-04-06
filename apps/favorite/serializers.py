from rest_framework import serializers
from .models import WishlistAlbum, HouseFavorite


class HouseFavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = HouseFavorite
        fields = ('id', 'wishlist_album', 'housing')


class WishlistAlbumSerializer(serializers.ModelSerializer):
    houseFavorite = HouseFavoriteSerializer(many=True, read_only=True)
    favorite_count = serializers.SerializerMethodField()

    def get_favorite_count(self, obj):
        return obj.houseFavorite.count()

    class Meta:
        model = WishlistAlbum
        fields = ('id', 'user', 'title', 'favorite_count', 'houseFavorite',)
