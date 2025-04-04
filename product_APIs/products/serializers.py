from rest_framework import serializers
from . import models 


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
        fields = ("name", "description", "price","category", "subcategory", "in_stock", "reviews",  "stock_count", "average_rating", "image" )

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name", read_only=True)
    class Meta:
        model = models.CartItem
        fields = ("product_name", "quantity")


class ShoppingCartSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username',read_only=True)
    cart_items = CartItemSerializer(many=True)
    class Meta:
        model = models.ShoppingCart
        fields = ("user", "total_price", "cart_items", "last_update_date", "created_at_date")

class OrderItemLogSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name")
    class Meta:
        model = models.OrderItemLog
        fields = ("product_name", "quantity", "unit_price_at_purchase","total_price_at_purchase")


class OrdersLogSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username',read_only=True)
    order_items = OrderItemLogSerializer(many=True, read_only=True)
    class Meta:
        model = models.OrdersLog
        fields =("user", "order_items", "total_price", "created_at_date")

class AddToCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    # make sure that quantity is always bigger than 0
    quantity = serializers.IntegerField(min_value=1)

    # check if the product actually exists and in stock
    def validate_product_id(self, value):
        try:
            product = models.Product.objects.get(id=value)
            if not product.in_stock:
                raise serializers.ValidationError("Product is not in stock.")
        except models.Product.DoesNotExist:
            raise serializers.ValidationError("Product not found.")
        return value

    # check if the requested quantity is smaller than or equal to the current stock 
    def validate(self, attrs):
        product = models.Product.objects.get(id=attrs['product_id'])
        user = self.context['request'].user
        requested_qty = attrs['quantity']

        # Check existing quantity in cart
        existing_qty = 0
        if hasattr(user, 'shopping_cart'):
            cart_item = user.shopping_cart.cart_items.get(product=product)
            if cart_item:
                existing_qty = cart_item.quantity

        # Check stock availability
        if (existing_qty + requested_qty) > product.stock_count:
            # check the available and return it with an error
            available = product.stock_count - existing_qty
            raise serializers.ValidationError(
                f"Only {available} item(s) available. You already have {existing_qty} in your cart."
            )

        return attrs
    
class CartItemUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CartItem
        fields = ['quantity']

    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Quantity cannot be negative")
        return value
    
    # Ensures requested quantity <= available stock
    def validate(self, attrs):
        # Current cart item being updated
        cart_item_instance = self.instance
        product = cart_item_instance.product
        new_quantity = attrs.get('quantity', cart_item_instance.quantity)

        if new_quantity > product.stock_count:
            raise serializers.ValidationError(
                f"Only {product.stock_count} items available in stock"
            )

        return attrs