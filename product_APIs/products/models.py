from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    # this will get updated with signals later
    # TODO : make the signals for updating count
    count = models.IntegerField(default=0)

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    main_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")

class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=500)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name="products")
    subcategory = models.ForeignKey(SubCategory, null=True, on_delete=models.SET_NULL, related_name="products")
    stock_count = models.IntegerField()
    # will not store the images on the database but only the reference because
    # https://www.geeksforgeeks.org/python-uploading-images-in-django/
    image =  models.ImageField(upload_to='images/')
    last_update_date = models.DateField(auto_now=True)
    created_at_date = models.DateField(auto_now_add=True)


