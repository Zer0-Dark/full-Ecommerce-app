from rest_framework import generics
from . import serializers
from . import models



class ProductsListAPIView(generics.ListAPIView):
    queryset= models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


