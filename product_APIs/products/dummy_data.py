import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'product_APIs.settings')
import django
django.setup()
import random
from faker import Faker
from django.contrib.auth import get_user_model
from products.models import (
    Category, SubCategory, Product, 
    Reviews, ShoppingCart, CartItem,
    OrdersLog, OrderItemLog
)

fake = Faker()
User = get_user_model()

def create_users(num=5):
    users = []
    for _ in range(num):
        user = User.objects.create_user(
            username=fake.unique.user_name(),
            email=fake.unique.email(),
            password="testpass123"
        )
        # Create shopping cart for each user
        ShoppingCart.objects.create(user=user)
        users.append(user)
    return users

def create_categories():
    categories = [
        ("Electronics", "Devices and gadgets"),
        ("Books", "Physical and digital books"),
        ("Clothing", "Apparel for all ages"),
        ("Home", "Furniture and decor"),
        ("Toys", "Children's toys and games")
    ]
    return [Category.objects.create(name=name, description=desc) for name, desc in categories]

def create_subcategories(categories):
    subcategories = [
        ("Laptops", categories[0]),
        ("Smartphones", categories[0]),
        ("Fiction", categories[1]),
        ("Non-Fiction", categories[1]),
        ("Men's Wear", categories[2]),
        ("Women's Wear", categories[2]),
        ("Furniture", categories[3]),
        ("Board Games", categories[4])
    ]
    return [
        SubCategory.objects.create(
            name=name,
            main_category=category,
            description=fake.sentence()
        ) for name, category in subcategories
    ]

def create_products(categories, subcategories, num=20):
    products = []
    for _ in range(num):
        category = random.choice(categories)
        available_subs = [s for s in subcategories if s.main_category == category]
        subcategory = random.choice(available_subs) if available_subs else None
        
        product = Product.objects.create(
            name=f"{fake.word().capitalize()} {random.choice(['Pro', 'Max', 'Lite', 'Plus'])}",
            description=fake.paragraph(),
            price=round(random.uniform(10, 1000), 2),
            category=category,
            subcategory=subcategory,
            stock_count=random.randint(0, 100),
            in_stock=random.choice([True, False]),
            image="images/default_product.jpg" 
        )
        products.append(product)
    return products

def create_reviews(products, users):
    for product in products:
        # Get 2-5 unique reviewers per product
        reviewers = random.sample(users, k=random.randint(2, min(5, len(users))))
        for user in reviewers:
            Reviews.objects.create(
                product=product,
                reviewer=user,
                rating=random.randint(1, 5),
                review=fake.paragraph()
            )

def create_cart_items(users, products):
    for user in users:
        cart = user.shopping_cart
        # Add 1-5 random products to cart
        for product in random.sample(products, k=random.randint(1, 5)):
            CartItem.objects.create(
                shopping_cart=cart,
                product=product,
                quantity=random.randint(1, 3)
            )

def create_orders(users, products):
    for user in users:
        # Create 1-3 orders per user
        for _ in range(random.randint(1, 3)):
            order = OrdersLog.objects.create(
                user=user,
                status=random.choice(["completed", "canceled"])
            )
            
            # Add 1-5 products to order
            selected_products = random.sample(products, k=random.randint(1, 5))
            for product in selected_products:
                price = product.price
                quantity = random.randint(1, 3)
                
                OrderItemLog.objects.create(
                    order_log=order,
                    product=product,
                    quantity=quantity,
                    unit_price_at_purchase=price,
                    total_price_at_purchase=price * quantity
                )


print("Creating users...")
users = create_users(5)

print("Creating categories...")
categories = create_categories()

print("Creating subcategories...")
subcategories = create_subcategories(categories)

print("Creating products...")
products = create_products(categories, subcategories, 20)

print("Creating reviews...")
create_reviews(products, users)

print("Creating cart items...")
create_cart_items(users, products)

print("Creating orders...")
create_orders(users, products)

print("Dummy data generation complete!")

