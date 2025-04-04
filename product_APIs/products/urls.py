from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductsListAPIView.as_view(), name="all-products"),
    path("AddToCart/", views.AddToCartAPIView.as_view(), name="add-to-cart"),
    path("MyCart/", views.ShoppingCartAPIView.as_view(), name="retrieve-cart"),
    path("UpdateMyCart/product/<int:pk>/", views.CartItemUpdateDeleteAPIView.as_view(), name="retrieve-update-delete-cart-item"),
]
