from rest_framework import serializers
from . import models 
from django.contrib.auth import get_user_model

User = get_user_model()

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubCategory
        fields = ("name", "description")


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubCategorySerializer(many=True, read_only=True)
    class Meta:
        model = models.Category
        fields = ("name", "description", "count", "subcategories")

class ReviewsSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source="product.name")
    reviewer = serializers.CharField(source='reviewer.username',read_only=True)
    class Meta:
        model = models.Reviews
        fields = ("rating", "review", "product", "reviewer", "last_update_date", "created_at_date")

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="category.name")
    subcategory = serializers.CharField(source="subcategory.name")
    reviews = ReviewsSerializer(many=True, read_only= True)

    class Meta:
        model = models.Product
        fields = ("name", "description", "price", "reviews", "category", "subcategory", "stock_count", "average_rating", "image" )


class ShoppingCartSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username',read_only=True)
    class Meta:
        model = models.ShoppingCart
        fields = ("user", "total_price", "cart_items", "last_update_date", "created_at_date")

class OrdersLogSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username',read_only=True)
    class Meta:
        model = models.OrdersLog
        fields =("user", "order_items", "total_price", "created_at_date")