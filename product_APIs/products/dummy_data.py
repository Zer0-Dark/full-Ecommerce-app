import random
from faker import Faker
from django.contrib.auth import get_user_model
from products.models import Category, SubCategory, Product, Reviews

fake = Faker()
User = get_user_model()

# Create multiple users
users = []
for _ in range(5):
    unique_email = fake.unique.email()  # Ensures the email is unique
    user = User.objects.create_user(username=fake.user_name(), email=unique_email, password="testpass123")
    users.append(user)

if not users:
    raise ValueError("No users were created. Check user creation logic!")

# Create multiple categories
categories_data = ["Electronics", "Books", "Clothing", "Home Appliances", "Toys"]
categories = [Category.objects.create(name=cat, description=fake.sentence()) for cat in categories_data]

# Create multiple subcategories
subcategories_data = [
    {"name": "Laptops", "category": categories[0]},
    {"name": "Smartphones", "category": categories[0]},
    {"name": "Fiction", "category": categories[1]},
    {"name": "Non-fiction", "category": categories[1]},
    {"name": "Men's Clothing", "category": categories[2]},
    {"name": "Women's Clothing", "category": categories[2]},
    {"name": "Kitchen", "category": categories[3]},
    {"name": "Toys for Kids", "category": categories[4]},
]
subcategories = [
    SubCategory.objects.create(name=sub["name"], description=fake.sentence(), main_category=sub["category"])
    for sub in subcategories_data
]

# Create multiple products
products = []
for _ in range(20):  # Create 20 products
    category = random.choice(categories)
    subcategory = random.choice([sub for sub in subcategories if sub.main_category == category])
    product = Product.objects.create(
        name=fake.word().capitalize() + " " + random.choice(["Pro", "Max", "Ultra", "Lite"]),
        description=fake.text(),
        price=round(random.uniform(10, 1000), 2),
        category=category,
        subcategory=subcategory,
        stock_count=random.randint(5, 50),
        average_rating=round(random.uniform(3.0, 5.0), 1),
        image="images/sample.jpg",
    )
    products.append(product)

# Create multiple reviews (Fixed issue with picking a random product)
for product in products:
    for _ in range(random.randint(2, 5)):  # Each product gets 2 to 5 reviews
        Reviews.objects.create(
            reviewer=random.choice(users),  #
            product=product,  
            review=fake.text(),  
            rating=random.randint(0, 5)
        )

print("Categories, subcategories, products, and reviews added successfully!")
