from django.urls import path
from .views import cart, checkout, contact, detail, index, shop
urlpatterns = [
    path("", index, name="index"),
    path("cart/", cart, name="cart"),
    path("checkout/", checkout, name="checkout"),
    path("contact/", contact, name="contact"),
    path("shop/", shop, name="shop"),
    path("detail/<int:product_id>/", detail, name="detail"),

]