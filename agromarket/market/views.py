from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Review
from django.utils.translation import gettext as _

def index(request):
    products = Product.objects.all()
    return render(request, 'market/index.html', {'products': products})

def produckt_list(request):
    products = Product.objects.all()
    return render(request, 'market/product_list.html', {'products': products})

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'market/review.html', {'reviews': reviews})
                  
def chat_page(request):
    return render(request, 'market/chat.html')
