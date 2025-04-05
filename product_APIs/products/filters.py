import django_filters
from .models import Product, Reviews

class ProductFilter(django_filters.FilterSet):
    # Use a custom method filter for category
    category = django_filters.CharFilter(method='filter_category')
    # And for subcategory
    subcategory = django_filters.CharFilter(method='filter_subcategory')

    # Price range filters
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    # Rating filters
    min_average_rating = django_filters.NumberFilter(field_name='average_rating', lookup_expr='gte')

    # make it so that you can look up the categories and sub categories using either id or the actual name
    def filter_category(self, queryset, name, value):
        # If the value is numeric, filter by category ID; otherwise, filter by category name.
        if value.isdigit():
            return queryset.filter(category__id=value)
        return queryset.filter(category__name__icontains=value)

    def filter_subcategory(self, queryset, name, value):
        # check if the value is numeric for subcategory.
        if value.isdigit():
            return queryset.filter(subcategory__id=value)
        return queryset.filter(subcategory__name__icontains=value)

    class Meta:
        model = Product
        fields = ['category', 'subcategory', 'in_stock', 'min_price', 'max_price',"min_average_rating"]


class ReviewFilter(django_filters.FilterSet):
    min_rating = django_filters.filters.NumberFilter(field_name="rating", lookup_expr='gte')
    
    class Meta:
        model = Reviews
        fields = ['product', 'reviewer', 'min_rating']
