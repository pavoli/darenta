from django.shortcuts import render

# Create your views here.
from .models import *


def products(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'eshop/products.html', context)
