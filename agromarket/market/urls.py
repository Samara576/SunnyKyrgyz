from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.product_list, name='product_list'),
    path('reviews/', views.review_page, name='review_page'),
    path('chat/', views.chat_page, name='chat_page'),
]