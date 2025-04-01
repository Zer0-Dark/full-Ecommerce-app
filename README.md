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
- [ ] Implement user registration and login  
    - [x] Implement simple JWT with rotations and blacklists
    - [x] CustomUser serializers

### 🛒 Product Management  
- [ ] Add product reviews  
- [ ] Implement shopping cart functionality  
- [ ] Create an orders log  
- [ ] Use Django signals to track products in specific categories  

### 🔌 API Endpoints  
- [ ] Design and document RESTful API endpoints  

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
```bash
python manage.py migrate
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


