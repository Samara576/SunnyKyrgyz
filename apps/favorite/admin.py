from django.contrib import admin
from .models import HouseFavorite, WishlistAlbum


@admin.register(HouseFavorite)
class HouseFavoriteAdmin(admin.ModelAdmin):
    list_display = ('housing', 'wishlist_album')
    list_filter = ('housing', 'wishlist_album')


@admin.register(WishlistAlbum)
class WishlistAlbumAdmin(admin.ModelAdmin):
    list_display = ('user', 'title')
    list_filter = ('user', 'title')
