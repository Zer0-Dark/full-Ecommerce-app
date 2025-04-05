# E-Market APIs

## 📌 Description  
E-Market APIs is a backend project built using **Django Rest Framework (DRF)** to serve as the foundation for a **full-stack e-commerce platform**.  
This project is also the **capstone** for the **ALX Software Engineering program**, focusing on:  
✅ User authentication  
✅ Product management  
✅ Order processing  
✅ Payment integration  

---

## 🔌 API Endpoints  


## Authentication

| Method | Endpoint                | Description                     | Auth Required |
|--------|-------------------------|---------------------------------|---------------|
| POST   | `/login/`               | User login                      | No            |
| POST   | `/register/`            | User registration               | No            |
| POST   | `/logout/`              | User logout                     | Yes           |
| POST   | `/api/token/refresh/`   | Refresh access token            | yes           |

---

## Products

### List Products
**Endpoint**: `GET /products/`

**Parameters**:
- `category` (string/int): Filter by category name or ID
- `subcategory` (string/int): Filter by subcategory name or ID
- `search` (string): Full-text search query for `product.name` and `product.description`
- `min_average_rating` (float): Minimum rating (0-5)
- `ordering` (string): Sort field (`price`, `-price`, etc)
- `page` (int): Page number
- `page_size` (int): Items per page

**Examples**:
### Paginated list
`GET /products/?page=1&page_size=20`

### Filtered search
`GET /products/?category=Electronics&subcategory=Laptops&min_average_rating=4`

### Sorted results
`GET /products/?ordering=-price`

---

## Shopping Cart

### Cart Management
| Method | Endpoint          | Description                      |
|--------|-------------------|----------------------------------|
| GET    | `/cart/`          | Get user's cart                  |
| DELETE | `/cart/clear/`    | Clear all cart items             |

### Cart Items
| Method | Endpoint                | Description                      |
|--------|-------------------------|----------------------------------|
| POST   | `/cart/items/`          | Add new item to cart             |
| GET    | `/cart/items/<int:pk>/` | Get specific cart item           |
| PATCH  | `/cart/items/<int:pk>/` | Update cart item quantity        |
| DELETE | `/cart/items/<int:pk>/` | Remove item from cart            |

**Request Format**:
```json
{
  "product_id": 1,
  "quantity": 2
}
```

**Example**:

POST /cart/items/
Content-Type: application/json
Authorization: Bearer <token>

```json
{
  "product_id": 5,
  "quantity": 3
}
```

### Checkout & Orders
#### Checkout
Endpoint: `POST /cart/checkout/`

Response:
```json
{
  "id": 123,
  "status": "completed",
  "total_price": "199.99",
  "order_items": [
    {
      "product_name": "Wireless Headphones",
      "quantity": 2,
      "unit_price_at_purchase": "99.99",
      "total_price_at_purchase": "199.98"
    }
  ]
}
```

### Order History

Endpoint: `GET /log/`

Parameters:

- `page` (int): Page number

- `page_size` (int): Items per page

## Request Requirements
Authentication: Required for all endpoints except:

`/login/`

`/register/`

`/api/token/refresh/`


## Review Management

### List/Create Reviews
**Endpoint**: `GET/POST /reviews/`

**GET Parameters**:
- `product`: Filter by product ID
- `ordering`: Sort by `-created_at_date` (newest first) or `rating`

**POST Request Body**:
```json
{
    "product": 1,
    "rating": 5,
    "review": "Excellent product!"
}
```
#### Response:
```json
{
    "id": 123,
    "product_name": "Wireless Headphones",
    "reviewer_username": "techlover123",
    "rating": 5,
    "review": "Excellent product!",
    "created_at_date": "2023-07-20"
}
```
---

## 🚀 Features (Planned & In Progress)  

## Security
- [x] JWT Authentication required for mutations

## 🧑‍💻 User Management  
- [x] Expand the user model to include profile pictures  
    - [x] add custom backend for allowing email/phone number login 
- [x] Implement user registration and login  
    - [x] Implement simple JWT with rotations and blacklists
    - [x] CustomUser serializers

## 🛒 Product Management  
- [x] Add product filters and pagination
- [x] Add product reviews  
- [x] Implement shopping cart functionality  
- [x] Create an orders log  

- [ ] Use Django signals to track products in specific categories  



### 💳 Payment Integration  
- [ ] Integrate a secure payment gateway  
    - [ ] stripe integration

### 📦 Deployment  
- [ ] Set up production-ready deployment
    - [ ] DEBUG= False
    - [ ] ALLOWED_HOSTS
    - [ ] SSL, HTTPS
    - [ ] Collect static files
- [ ] choose a hosting provider
    - AWS or DigitalOcean or Heroku or pythonanywhere
- [ ] setup server 
- [ ] Handle static & media files
- [ ] setup Domain, SSl
- [ ] setup monitoring 
---

## 🛠 Installation & Setup  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/yourusername/E_Market_APIs.git
cd E_Market_APIs
```
### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set up environment variables in .env:
```bash
SECRET_KEY=your_secret_key
```
you can generate one with :
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

### 5️⃣ Run Migrations
### Read Carefully!!!

```bash
python manage.py migrate
```

when running migration you might face an issue regarding the current date as there was no default provided to prepare for a production environment 
you will be prompted to choose one of 2 options 

`1) Provide a one-off default now (will be set on all existing rows with a null value for this column)`
`2) Quit and manually define a default value in models.py.`

just choose the 1) and proceed to provide `timezone.now`

#### (optional) Temp data
you can run a script in product_APIs/products/dummy_data.py
by running 

```bash
python manage.py shell < products/dummy_data.py 
```

###  Start the Development Server
```bash
python manage.py runserver
```

---

### 📜 License
This project is licensed under the MIT License.
Feel free to use and modify!

---

### ✨ Stay Tuned!
This project is evolving—new features and improvements are on the way!
⭐ Star the repository to get updates.


