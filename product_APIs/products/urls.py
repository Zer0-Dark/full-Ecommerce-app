from django.urls import path
from . import views

urlpatterns = [
    # products urls
    # list all products with filters and pagination 
    path("products/", views.ProductsListAPIView.as_view(), name="all-products"),
    
    # reviews urls 
    path("reviews/", views.ReviewListCreateAPIView.as_view(), name="list-create-review"),


    # cart urls
    # get the current logged in user cart
    path("cart/", views.ShoppingCartAPIView.as_view(), name="retrieve-cart"),
    # create a new cart item and update the quantity if it already exists
    path("cart/items/", views.CartItemCreateAPIView.as_view(), name="cartitem-create"),
    # retrieve a specific cart item / Update it / delete it (pk = cart item id)
    path("cart/items/<int:pk>/", views.CartItemUpdateDeleteAPIView.as_view(), name="retrieve-update-delete-cart-item"),
    # delete all items in the logged in user cart 
    path("cart/clear/", views.CartDeleteAPIView.as_view(), name="cart-clear"),
    # checkout the current cart and add the orders to the log
    path('cart/checkout/', views.CheckoutAPIView.as_view(), name='checkout'),
    # return all the current user purchase logs
    path("log/", views.OrderLogAPIView.as_view(), name="all-logs"),

]
