from django.contrib import admin

from .models import CustomUser, ReviewSite, Profile

admin.site.register(CustomUser)
admin.site.register(ReviewSite)
admin.site.register(Profile)