from rest_framework import serializers
from .models import Advertising
from .service import create_slug


class AdvertisingSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Advertising
        fields = ("id", "housing", "added", "slug")

    def create(self, validated_data):
        return create_slug(self, validated_data)
