from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

User = get_user_model()


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
    price = models.DecimalField(decimal_places=2, max_digits=8, validators=[MinValueValidator(0)])
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name="products")
    subcategory = models.ForeignKey(SubCategory, null=True, on_delete=models.SET_NULL, related_name="products")
    stock_count = models.IntegerField(validators=[MinValueValidator(0)])
    # TODO: make signal to update this on every review relevant to the product 
    average_rating = models.DecimalField(max_digits=2, decimal_places=1,validators=[MaxValueValidator(5.0), MinValueValidator(0.0)])
    # will not store the images on the database but only the reference because
    # https://www.geeksforgeeks.org/python-uploading-images-in-django/
    image =  models.ImageField(upload_to='images/')
    last_update_date = models.DateField(auto_now=True)
    created_at_date = models.DateField(auto_now_add=True)

class Reviews(models.Model):
    # from zero to five (exact numbers)
    rating = models.IntegerField( validators=[MaxValueValidator(5), MinValueValidator(0)])
    review = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    last_update_date = models.DateField(auto_now=True)
    created_at_date = models.DateField(auto_now_add=True)

class ShoppingCart(models.Model):
    # cart items will be decoupled from the shoppingCart model and use a foreign key instead 
    # each user has only one cart
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="shopping_cart")
    last_update_date = models.DateTimeField(auto_now=True)
    created_at_date = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return sum(item.total_price for item in self.cart_items.all())

class CartItem(models.Model):
    # should include the userID, productID(s), Total Price,Etc
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, related_name="cart_items")
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(0)])

    class Meta:
        # this makes sure that each shopping cart doesn't have duplicate products just an increment on quantity
        unique_together = ('shopping_cart', 'product')
    
    @property
    def total_price(self):
        return self.product.price * self.quantity

class OrdersLog(models.Model):
    # TODO expand the user model first
    # should include the userID, productID(s), Total Price, timestamp of the purchase, Etc
    pass

