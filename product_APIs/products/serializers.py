from rest_framework import serializers
from . import models 


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ("name", "description", "price", "category", "subcategory", "stock_count", "average_rating", "image" )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ("name", "description", "count", "subcategories")

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reviews
        fields = ("rating", "review", "product", "reviewer", "last_update_date", "created_at_date")

class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ShoppingCart
        fields = ("user", "total_price", "cart_items", "last_update_date", "created_at_date")

class OrdersLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrdersLog
        fields =("user", "order_items", "total_price", "created_at_date")