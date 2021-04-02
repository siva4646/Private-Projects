from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# /products call index() function
# URL (Uniform Resource Locator) (Address)
def index(request):
    # Product.objects.save() Save/Update existing product
    products = Product.objects.all()
    return render(  request
                  , 'index.html'
                  , {'products': products})


def new(request):
    return HttpResponse("New Products")