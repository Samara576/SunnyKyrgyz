from django.contrib import admin
from .models import HousingReview, HousingReservation, Room, HousingImage, RoomImage, Housing, HousingAvailability


@admin.register(HousingAvailability)
class HousingAvailability(admin.ModelAdmin):
    list_display = ('rooms', 'date', 'is_available')
    list_filter = ('rooms', 'date', 'is_available')
    search_fields = ('rooms', 'date', 'is_available')


class HousingImageInline(admin.TabularInline):
    model = HousingImage
    min_num = 5
    max_num = 20
    extra = 0

    class Meta:
        model = Housing
        fields = '__all__'


@admin.register(Housing)
class HousingAdmin(admin.ModelAdmin):
    list_display = ('housing_name', 'address', 'housing_type', 'accommodation_type', 'food_type')
    list_filter = ('housing_type', 'region', 'stars', 'food_type')
    search_fields = ('housing_name', 'address')
    prepopulated_fields = {'slug': ('housing_name',)}
    inlines = (HousingImageInline,)


@admin.register(HousingReservation)
class HousingReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'housing', 'check_in_date',
                    'check_out_date', 'adults', 'children', 'get_total_guests')
    list_filter = ('check_in_date', 'check_out_date')
    search_fields = ('user__username', 'housing__housing_name')

    def get_total_guests(self, obj):
        return obj.adults + obj.children


@admin.register(HousingReview)
class HousingReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'housing', 'staff_rating', 'comfort_rating', 'cleanliness_rating',
                    'value_for_money_rating', 'food_rating', 'location_rating', 'date_added')
    list_filter = ('staff_rating', 'comfort_rating', 'cleanliness_rating', 'value_for_money_rating', 'food_rating',
                   'location_rating')
    search_fields = ('user__username', 'housing__housing_name')


class RoomImageInline(admin.TabularInline):
    model = RoomImage
    min_num = 5
    max_num = 20
    extra = 0


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('housing', 'room_name', 'price_per_night', 'max_guest_capacity', 'room_area')
    list_filter = ('housing', 'room_name', 'smoking_allowed')
    search_fields = ('housing__housing_name', 'room_name')
    inlines = (RoomImageInline,)
