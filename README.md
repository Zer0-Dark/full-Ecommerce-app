# E-Market APIs

## 📌 Description  
E-Market APIs is a backend project built using **Django Rest Framework (DRF)** to serve as the foundation for a **full-stack e-commerce platform**.  
This project is also the **capstone** for the **ALX Software Engineering program**, focusing on:  
✅ User authentication  
✅ Product management  
✅ Order processing  
✅ Payment integration  

---

## 🚀 Features (Planned & In Progress)  

### 🧑‍💻 User Management  
- [x] Expand the user model to include profile pictures  
    - [x] add custom backend for allowing email/phone number login 
- [x] Implement user registration and login  
    - [x] Implement simple JWT with rotations and blacklists
    - [x] CustomUser serializers

### 🛒 Product Management  
- [x] Add product reviews  
    - [x] product reviews serializer
- [x] Implement shopping cart functionality  
    - [x] serializer
- [x] Create an orders log  
    - [x] serializer 
- [ ] Use Django signals to track products in specific categories  

### 🔌 API Endpoints  
- [ ] Design and document RESTful API endpoints  

#### list all products with reviews
```bash
/products/?page=(the page number without the ())&page_size=(the size you want without the () )
example : /products/?page=1&page_size=50
```

```bash
/products/?category=Electronics&subcategory=Laptops&page=2&page_size=1
or
/products/?category=1&subcategory=1&page=2&page_size=1
or
/products/?category=Electronics&subcategory=Laptops&min_average_rating=4
or
/products/?search=Really+Max
or
descending
/products/?ordering=-price
```

### 💳 Payment Integration  
- [ ] Integrate a secure payment gateway  

### 📦 Deployment  
- [ ] Set up production-ready deployment  

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
### 4️⃣ Run Migrations
### Read Carefully!!!

```bash
python manage.py migrate
```

when running migration you might face an issue regarding the current date as there was no default provided to prepare for a production environment 
you will be prompted to choose one of 2 options 
```bash
1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
2) Quit and manually define a default value in models.py.
```
just choose the 1) and proceed to provide `timezone.now`

#### (optional) Temp data
you can run a script in product_APIs/products/dummy_data.py
by running 

```bash
python manage.py shell < products/dummy_data.py 
```

### 5️⃣ Start the Development Server
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


