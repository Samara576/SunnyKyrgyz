from rest_framework import serializers
from .models import Transfer, TransferReservation, TransferReview, TransferImage
from .constants import DESTINATION_CHOICES, SAFETY_EQUIPMENT_CHOICES, AMENITIES_CHOICES
from .service import get_average_rating, update_operating_area


class TransferReviewSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    date_added = serializers.DateField(format='%d-%m-%Y', read_only=True)

    class Meta:
        model = TransferReview
        fields = ('id', 'user', 'transfer', 'comment', 'date_added', 'how_it_went',
                  'comfortable_driving', 'technical_condition', 'cleanliness_level',
                  'price_quality_ratio', 'safety_level')


class TransferImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferImage
        fields = ('id', 'image', 'transfer')


class TransferSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField(read_only=True)
    operating_area = serializers.MultipleChoiceField(choices=DESTINATION_CHOICES + (('По всему КР', 'По всему КР'),),
                                                     label="Территории эксплуатации")
    amenities = serializers.MultipleChoiceField(choices=AMENITIES_CHOICES, label="Внутренние удобства")
    safety_equipment = serializers.MultipleChoiceField(choices=SAFETY_EQUIPMENT_CHOICES, label="Система безопасности")
    transfer_images = TransferImageSerializer(many=True, read_only=True, )
    reviews = TransferReviewSerializer(many=True, read_only=True, label="Отзывы")

    class Meta:
        model = Transfer
        fields = ('id', 'brand', 'description', 'category', 'body_type', 'transmission', 'steering', 'drive_type',
                  'fuel_type', 'color', 'passenger', 'condition', 'fuel_consumption', 'minimum_age',
                  'passenger_sits', 'year', 'driving_experience', 'amenities', 'safety_equipment',
                  'pickup_location', 'return_location', 'check_in_time', 'check_out_time',
                  'can_arrange_pickup_return', 'driver_service', 'operating_area', 'currency',
                  'rental_price', 'transfer_images', 'reviews', 'average_rating')

    def get_average_rating(self, obj):
        return get_average_rating(obj, obj)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data = update_operating_area(data)
        return data


class TransferReservationSerializer(serializers.ModelSerializer):
    pickup_date = serializers.DateField(format='%d-%m-%Y')
    return_date = serializers.DateField(format='%d-%m-%Y')

    class Meta:
        model = TransferReservation
        fields = ('id', 'user', 'transfer', 'transfer_location', 'destination_location',
                  'pickup_date', 'return_date', 'pickup_time', 'return_time',
                  'return_location', 'different_pickup_places', 'with_driver')
