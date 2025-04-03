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

    def __str__(self):
        return f"Category: {self.name}"

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    main_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")

    def __str__(self):
        return f"{self.name}, subcategory of {self.main_category}"

class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=500)
    price = models.DecimalField(decimal_places=2, max_digits=8, validators=[MinValueValidator(0)])
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name="products")
    subcategory = models.ForeignKey(SubCategory, null=True, on_delete=models.SET_NULL, related_name="products")
    stock_count = models.IntegerField(validators=[MinValueValidator(0)])
    # TODO: make signal to update this on every review relevant to the product 
    # default=0.0 here was add to avoid an issue during making migrations but it won't ever be the default value
    average_rating = models.DecimalField(max_digits=2, decimal_places=1,validators=[MaxValueValidator(5.0), MinValueValidator(0.0)], default=0.0)
    # will not store the images on the database but only the reference because
    # https://www.geeksforgeeks.org/python-uploading-images-in-django/
    image =  models.ImageField(upload_to='images/')
    #  null=True was added to avoid issues with existing records but it will never be null
    last_update_date = models.DateField(auto_now=True, null=True)
    created_at_date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f"product: {self.name}"

class Reviews(models.Model):
    # from zero to five (exact numbers)
    rating = models.IntegerField( validators=[MaxValueValidator(5), MinValueValidator(0)], default=0.0)
    review = models.TextField(null=True)
    # default=1 here was add to avoid an issue during making migrations but it won't ever be the default value
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews", default=1)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews", default=1)
    #  null=True was added to avoid issues with existing records but it will never be null
    last_update_date = models.DateField(auto_now=True, null=True)
    created_at_date = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return f"review of  user {self.reviewer}, score: {self.review}"

class ShoppingCart(models.Model):
    # cart items will be decoupled from the shoppingCart model and use a foreign key instead 
    # each user has only one cart
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="shopping_cart", default=1)
    #  null=True was added to avoid issues with existing records but it will never be null
    last_update_date = models.DateTimeField(auto_now=True, null=True)
    created_at_date = models.DateTimeField(auto_now_add=True, null=True)

    @property
    def total_price(self):
        return sum(item.total_price for item in self.cart_items.all())
    
    def __str__(self):
        return f"shopping cart of {self.user}"

class CartItem(models.Model):
    # should include the productID(s), Total Price,Etc
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE, related_name="cart_items")
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(0)])

    class Meta:
        # this makes sure that each shopping cart doesn't have duplicate products just an increment on quantity
        unique_together = ('shopping_cart', 'product')
    
    @property
    def total_price(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"{self.quantity} {self.product} from  shopping cart #{self.shopping_cart}"

class OrdersLog(models.Model):
    # should include the userID, productID(s), Total Price, timestamp of the purchase, Etc
    # default=1 here was add to avoid an issue during making migrations but it won't ever be the default value
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders", default=1)
    #  null=True was added to avoid issues with existing records but it will never be null
    created_at_date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=20, choices=[("completed", "Completed"), ("canceled", "Canceled")], default="completed")

    @property
    def total_price(self):
        return sum(item.total_price_at_purchase for item in self.order_items.all())
    
    def __str__(self):
        return f"OrderLog #{self.id} - {self.user.username} ({self.status})"
    
class OrderItemLog(models.Model):
    order_log = models.ForeignKey(OrdersLog, on_delete=models.CASCADE, related_name="order_items")
    
    product = models.ForeignKey("Product", on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()
    # this is a reminder for me that those prices are not dynamically linked because they are a snap shot of the price 
    # at the time of purchase (prices will go up :sad: )
    unit_price_at_purchase = models.DecimalField(max_digits=8, decimal_places=2)
    total_price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.product.name if self.product else 'Deleted Product'}"

