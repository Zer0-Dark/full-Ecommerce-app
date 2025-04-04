from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductsListAPIView.as_view(), name="all-products"),
    path("AddToCart/", views.AddToCartAPIView.as_view(), name="add-to-cart"),
]
