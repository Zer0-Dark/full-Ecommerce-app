from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.db.models import Avg
from .models import Product, Reviews

# Pre-save signal to capture the old category before a Product update
@receiver(pre_save, sender=Product)
def set_old_category(sender, instance, **kwargs):
    if instance.pk:
        try:
            instance._old_category = Product.objects.get(pk=instance.pk).category
        except Product.DoesNotExist:
            instance._old_category = None



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
            category.count = category.products.count()
            category.save()

    # If the product's category has changed, update the old category count
    old_category = getattr(instance, '_old_category', None)
    if old_category and old_category != instance.category:
        update_count(old_category)
    
    # Always update the count for the current category
    update_count(instance.category)