# Brewsko Bistro POS System

## Requirements
- Python 3.8+
- Django 4.x

## Installation & Setup

### 1. Install Django
```bash
pip install django
```

### 2. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Seed Initial Data
```bash
python setup_data.py
```

### 4. Start the Server
```bash
python manage.py runserver
```

### 5. Open Browser
```
http://127.0.0.1:8000
```

---

## Login Credentials

| Role    | Username | Password    |
|---------|----------|-------------|
| Admin   | admin    | admin123    |
| Cashier | cashier  | cashier123  |
| Kitchen | kitchen  | kitchen123  |

---

## System Features

### 🔐 Admin Panel (`/panel/`)
- **Dashboard** — Daily sales, order count, average order value, low stock alerts, weekly sales chart, hourly order trend
- **Manage Menu** — Add, edit, delete, toggle availability of menu items with 18 categories
- **Inventory** — Track stock levels with critical/low stock alerts (supports kg, L, pcs, pack)
- **Security** — Manage user accounts (Admin/Cashier/Kitchen roles) and view transaction history

### 🧾 Cashier Station (`/cashier/`)
- Welcome splash screen — tap to start new order
- Browse Foods and Drinks by category
- Item customization popup — Serving Style (food), Size/Temperature (drinks), Add-ons
- Real-time cart with quantity adjustments
- Dine-In / To-Go toggle
- Payment processing — Cash (with change calculation) and GCash (with reference number)
- Payment success receipt with order summary
- Payment error handling with retry

### 👨‍🍳 Kitchen Dashboard (`/kitchen/`)
- Live order board with 5-second auto-refresh
- Order status flow: Pending → Preparing → Ready → Completed
- Order cards with item details and customizations
- Real-time counters for Pending, Preparing, Ready, Total orders
- Live clock display
- Search/filter orders

---

## Menu Categories
**Foods:** Sizzling Steaks, Burger With Fries, Appetizer, Pasta, Grilled Rice Meals,
Sizzling Javalog 99ers, Sizzling Javalog Special, Brewsko Special, Wings With Fries,
The Ultimate Sisig, Pizza

**Drinks:** Coffee, Blended Drinks, Non-Coffee, Milk Tea, Refreshing, Hot Tea, Add Ons
