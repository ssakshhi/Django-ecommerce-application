from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.
def index(request):
    return render(request, template_name="index.html")

def checkout(request):
    return render(request, template_name="checkout.html")

def contact(request):
    return render(request, template_name="contact.html")

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        "products" : product,
    }
    return render(request, 'detail.html', context)

def shop(request):
    context = {
        "products" : Product.objects.all(),
    }
    return render(request, "shop.html", context)

def cart(request):
    return render(request, template_name="cart.html")