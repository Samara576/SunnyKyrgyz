from django.contrib.contenttypes.models import ContentType
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import HouseFavorite


class ManageFavorite:
    @action(
        detail=True,
        methods=['get'],
        url_path='favorite',
        permission_classes=[IsAuthenticated, ]
    )
    def favorite(self, request, pk):
        instance = self.get_object()
        content_type = ContentType.objects.get_for_model(instance)
        favorite_obj, created = HouseFavorite.objects.get_or_create(
            user=request.user, content_type=content_type, object_id=instance.id
        )

        if created:
            return Response(
                {'message': 'Объект добавлен в избранное'},
                status=status.HTTP_201_CREATED
            )
        else:
            favorite_obj.delete()
            return Response(
                {'message': 'Объект удален из избранного'},
                status=status.HTTP_200_OK
            )

