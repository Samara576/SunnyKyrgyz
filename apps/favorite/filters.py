from django_filters import FilterSet

from apps.favorite.models import WishlistAlbum


class WishlistFilters(FilterSet):
    class Meta:
        model = WishlistAlbum
        fields = ("user",)
