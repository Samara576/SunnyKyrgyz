from rest_framework.exceptions import ValidationError


def get_average_rating(self, obj):
    from apps.travel.models import HousingReview
    reviews = HousingReview.objects.filter(housing=obj)
    if reviews:
        total_rating = sum([
            (review.staff_rating +
             review.comfort_rating +
             review.cleanliness_rating +
             review.value_for_money_rating +
             review.food_rating +
             review.location_rating) / 6
            for review in reviews
        ])
        average_rating = total_rating / len(reviews)
        return round(average_rating, 1)
    return 0


def compress_image(self):
    from PIL import Image
    img = Image.open(self.image.path)
    if img != 'null':
        img = img.convert('RGB')
        img.thumbnail((800, 800))
        img.save(self.image.path, 'JPEG', quality=90)
    else:
        pass


def validate_beds(single_bed, double_bed, queen_bed, king_bed, sofa_bed):
    total_beds = (single_bed or 0) + (double_bed or 0) + (queen_bed or 0) + (king_bed or 0) + (sofa_bed or 0)
    if total_beds > 3:
        raise ValidationError("Общее количество кроватей не может превышать три.")


def validata_people(adults, children):
    total_people = (adults or 0) + (children or 0)
    if total_people > 6:
        raise ValidationError("Количество гостей н может быть больше шести")
    elif total_people < 1:
        raise ValidationError("Количество гостей не может быть равен 0")


def get_cheapest_room_price(self, obj):
    cheapest_room = obj.rooms.order_by('price_per_night').first()
    return cheapest_room.price_per_night if cheapest_room else None


def get_housing_image(self, obj):
    first_image = obj.housing_images.first()
    if first_image:
        return first_image.image.url
    else:
        return None
