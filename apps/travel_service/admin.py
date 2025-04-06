from django.contrib import admin
from .models import Transfer, TransferReservation, TransferReview, TransferImage


class TransferImageInline(admin.TabularInline):
    model = TransferImage
    min_num = 5
    max_num = 20
    extra = 0


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ('brand', 'category', 'body_type', 'transmission', 'rental_price', 'fuel_type', 'year',
                    'pickup_location')
    list_filter = ('brand', 'category', 'body_type', 'transmission', 'passenger', 'fuel_type', 'year',
                   'pickup_location')
    search_fields = ('brand', 'category', 'year', 'pickup_location')
    inlines = (TransferImageInline,)


@admin.register(TransferReservation)
class TransferReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'destination_location', 'transfer_location', 'pickup_date', 'pickup_time',
                    'return_location', 'return_date', 'return_time', 'with_driver')
    list_filter = ('user', 'transfer_location', 'destination_location', 'pickup_date', 'return_location', 'return_date',
                   'different_pickup_places')
    search_fields = ('user', 'transfer_location', 'destination_location')


@admin.register(TransferReview)
class TransferReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'transfer', 'comfortable_driving', 'technical_condition', 'cleanliness_level',
                    'price_quality_ratio', 'safety_level', 'how_it_went', 'date_added')
    list_filter = ('user', 'transfer')
    search_fields = ('user', 'transfer__brand', 'comment')
