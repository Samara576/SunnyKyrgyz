import django_filters
from .models import Transfer


class TransferFilter(django_filters.FilterSet):
    min_rental_price = django_filters.NumberFilter(field_name='rental_price', lookup_expr='gte')
    max_rental_price = django_filters.NumberFilter(field_name='rental_price', lookup_expr='lte')

    class Meta:
        model = Transfer
        fields = ('min_rental_price', 'max_rental_price', 'category', 'brand', 'passenger_sits', 'steering',
                  'fuel_type', 'color', 'drive_type', 'transmission', 'body_type', 'condition', 'amenities')
