from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Avg
from .models import Product, Reviews

# Signal for product average rating
# gets trigger on any change in Review (create/update/delete)
@receiver([post_save, post_delete], sender=Reviews)
def update_product_rating(sender, instance, **kwargs):
    product = instance.product
    avg_rating = Reviews.objects.filter(product=product).aggregate(
        avg_rating=Avg('rating')
    )['avg_rating'] or 0.0
    
    
    Product.objects.filter(id=product.id).update(
        average_rating=round(avg_rating, 1)
    )

# Signal for category product count
@receiver([post_save, post_delete], sender=Product)
def update_category_counts(sender, instance, **kwargs):
    def update_count(category):
        if category:
            # get the count from the product and give it to the count
            category.count = category.products.count()
            category.save()

    # Get both old and new categories if updating
    old_category = None
    if 'update_fields' not in kwargs or 'category' not in kwargs['update_fields']:
        try:
            old_product = Product.objects.get(id=instance.id)
            old_category = old_product.category
        except Product.DoesNotExist:
            pass

    # Update counts
    update_count(old_category)
    update_count(instance.category)