from rest_framework import generics
from . import serializers
from . import models
from rest_framework.pagination import PageNumberPagination
from .filters import ProductFilter

class ProductPagination(PageNumberPagination):
    page_size = 10  # 10 items per page (default)
    page_size_query_param = 'page_size'  # Allow users to specify their page size
    max_page_size = 100  # Max page size allowed

class ProductsListAPIView(generics.ListAPIView):
    queryset= models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    pagination_class = ProductPagination
    filterset_class  = ProductFilter
    search_fields = ['name']
