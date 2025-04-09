from django.contrib import admin
from .models import Category, Product, ChatMessage, Review

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ChatMessage)
admin.site.register(Review)
