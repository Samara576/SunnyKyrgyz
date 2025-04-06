from django.contrib import admin
from .models import Advertising


@admin.register(Advertising)
class AdvertisingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('housing',)}
