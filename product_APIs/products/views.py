from rest_framework import generics, status
from . import serializers
from . import models
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response 
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter

# customize the pagination from the endpoint 
class ProductPagination(PageNumberPagination):
    page_size = 10  # 10 items per page (default)
    page_size_query_param = 'page_size'  # Allow users to specify their page size
    max_page_size = 100  # Max page size allowed

class ProductsListAPIView(generics.ListAPIView):
    queryset= models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    pagination_class = ProductPagination
    # DjangoFilterBackend is already the global filter backend but i want to add SearchFilters as well
    filter_backends= [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class  = ProductFilter
    # this will make it so that you can search with those fields using the rest_framework.filters.SearchFilter
    search_fields = ['name', 'description']
    # uses rest_framework.filters.OrderingFilter to "order" 🥹🥹🥹
    ordering_fields = ['price']


class AddToCartAPIView(generics.GenericAPIView):
    # create a cart for the currently logged in user and add products accordingly 
    serializer_class = serializers.ShoppingCartSerializer
    permission_classes= [IsAuthenticated,]


    def post(self, request, *args, **kwargs):
        # Retrieve or Create a Shopping Cart:
            # When a user adds an item, we first ensure they have a shopping cart. If not, we create one.
        # Add or Update Cart Items:
            # If a CartItem for that product already exists in the cart (thanks to the unique_together constraint), simply update its quantity.
            # Otherwise, create a new CartItem.
        # Return the Updated Cart:
            # You can then return the updated cart serialized using your existing ShoppingCartSerializer.
        user = request.user

        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)  # Default to 1 if not provided

        try:
            quantity = int(quantity)
            if quantity < 1:
                return Response({"detail": f"quantity can't be lower than 1"}, status=status.HTTP_400_BAD_REQUEST )
        except (ValueError, TypeError):
            return Response({"detail":"invalid quantity"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            product = models.Product.objects.get(id= product_id)
            if not product.in_stock:
                return Response({"detail":"Product is not in stock"}, status=status.HTTP_400_BAD_REQUEST)
        except models.Product.DoesNotExist:
            return Response({"detail": "Product not found."}, status=status.HTTP_404_NOT_FOUND)
        
        # get or create a cart for the user
        cart, _ = models.ShoppingCart.objects.get_or_create(user=user)

        # get or create a cart item
        cart_item, created_item = models.CartItem.objects.get_or_create(product=product, shopping_cart=cart)

        if not created_item:
            cart_item.quantity += quantity
            cart_item.save()

        # Return the updated cart 
        serializer = self.get_serializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ShoppingCartAPIView(generics.RetrieveAPIView):
    serializer_class = serializers.ShoppingCartSerializer
    permission_classes = [IsAuthenticated,]

    def get_object(self):
        cart, created = models.ShoppingCart.objects.get_or_create(user=self.request.user)
        return cart