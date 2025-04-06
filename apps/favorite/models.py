from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from apps.users.email import CustomUser
from apps.travel.models import Housing


class HouseFavorite(models.Model):
    wishlist_album = models.ForeignKey("WishlistAlbum", on_delete=models.CASCADE, blank=True, null=True,
                                       related_name='houseFavorite')
    housing = models.ForeignKey(Housing, on_delete=models.CASCADE, related_name='housing')
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        unique_together = ("wishlist_album", "housing")
        verbose_name = "Избранное"
        verbose_name_plural = "Избранные"
        ordering = ['-id']
        constraints = [
            models.UniqueConstraint(
                fields=['wishlist_album', 'object_id', 'content_type'],
                name='unique_wishlist_album_content_type_object_id'
            )
        ]


class WishlistAlbum(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        unique_together = ('user', 'title')
        verbose_name = "Альбом желаний"
        verbose_name_plural = "Альбомы желаний"
        ordering = ['-id']
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'object_id', 'content_type'],
                name='unique_user_content_type_object_id'
            )
        ]

    def __str__(self):
        return self.title
