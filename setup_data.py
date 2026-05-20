#!/usr/bin/env python
"""
Brewsko Bistro POS - Initial Data Setup Script
Run: python setup_data.py
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'brewsko_pos.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from accounts.models import User
from panel.models import MenuItem, InventoryItem

print("Setting up Brewsko Bistro POS...")

# ── Users ──────────────────────────────────────────────
users = [
    ('admin',   'admin123',   'admin'),
    ('cashier', 'cashier123', 'cashier'),
    ('kitchen', 'kitchen123', 'kitchen'),
]
for username, password, role in users:
    if not User.objects.filter(username=username).exists():
        u = User.objects.create_user(username=username, password=password)
        u.role = role
        u.is_staff = (role == 'admin')
        u.is_superuser = (role == 'admin')
        u.save()
        print(f"  Created user: {username} / {password} [{role}]")
    else:
        print(f"  User already exists: {username}")

# ── Menu Items ─────────────────────────────────────────
menu_items = [
    # Sizzling Steaks
    ('Pork Steak 12oz',          165, 'Sizzling Steaks',          True,  False, False),
    ('Pork Steak Size',          165, 'Sizzling Steaks',          True,  False, False),
    ('Porkloin Steak',           165, 'Sizzling Steaks',          True,  False, False),
    ('Sirloin Steak',            165, 'Sizzling Steaks',          True,  False, False),
    ('T-Bone Steak Brewsko Size',165, 'Sizzling Steaks',          True,  False, False),
    # Burger With Fries
    ('BBQ Bacon Cheese Burger',  165, 'Burger With Fries',        False, False, False),
    ('Brewsko Cheese Burger',    165, 'Burger With Fries',        False, False, False),
    ('Cheesy Bacon Mushroom',    165, 'Burger With Fries',        False, False, False),
    ('Chicken Keto Burger',      165, 'Burger With Fries',        False, False, False),
    ('Slim-Bury Burger',         165, 'Burger With Fries',        False, False, False),
    # Appetizer
    ('Brewsko Nachos',           75,  'Appetizer',                False, False, False),
    ('Cheesy Bacon Fries',       75,  'Appetizer',                False, False, False),
    ('French Fries',             75,  'Appetizer',                False, False, False),
    # Pasta
    ('Piso Alfredo',             99,  'Pasta',                    False, False, False),
    ('Piso Spaghetti',           99,  'Pasta',                    False, False, False),
    # Grilled Rice Meals
    ('Adobo Pork',               99,  'Grilled Rice Meals',       False, False, False),
    ('BBQ Beef Ribs',            99,  'Grilled Rice Meals',       False, False, False),
    ('Sinigang Bangus',          99,  'Grilled Rice Meals',       False, False, False),
    ('Sinigang Mixed Bowls',     99,  'Grilled Rice Meals',       False, False, False),
    # Wings With Fries
    ('Ala Carte',                99,  'Wings With Fries',         False, False, False),
    ('Garlic Parmesan 6 pcs',    99,  'Wings With Fries',         False, False, False),
    ('Honey Glaze 6 pcs',        99,  'Wings With Fries',         False, False, False),
    ('NY Buffalo 6 pcs',         99,  'Wings With Fries',         False, False, False),
    # The Ultimate Sisig
    ('Bagnet Sisig',             99,  'The Ultimate Sisig',       False, False, False),
    ('Kapampangan Sisig',        99,  'The Ultimate Sisig',       False, False, False),
    ('Pork Sisig',               99,  'The Ultimate Sisig',       False, False, False),
    # Pizza
    ('Beef Curry Special',       99,  'Pizza',                    False, False, False),
    ('Breaded Special',          99,  'Pizza',                    False, False, False),
    ('Chicken Ala King',         99,  'Pizza',                    False, False, False),
    ('Grilled Chicken',          99,  'Pizza',                    False, False, False),
    ('Grilled Pork Chicken',     99,  'Pizza',                    False, False, False),
    ('Lemon Bacon',              99,  'Pizza',                    False, False, False),
    ('Oyster King Sauce',        99,  'Pizza',                    False, False, False),
    ('Pork Tonkatsu',            99,  'Pizza',                    False, False, False),
    ('Tery Katsu Ala King',      99,  'Pizza',                    False, False, False),
    # Brewsko Special
    ('Chicken Egg',              99,  'Brewsko Special',          False, False, False),
    ('Lechon Kawali',            99,  'Brewsko Special',          False, False, False),
    ('Manila Sisig',             99,  'Brewsko Special',          False, False, False),
    ('Machisig',                 99,  'Brewsko Special',          False, False, False),
    ('Pork Sisig BB',            99,  'Brewsko Special',          False, False, False),
    # Sizzling Javalog 99ers
    ('Sizzling Chicken',         99,  'Sizzling Javalog 99ers',  False, False, False),
    ('Sizzling Chicken Javalog', 99,  'Sizzling Javalog 99ers',  False, False, False),
    ('Sizzling Pork',            99,  'Sizzling Javalog 99ers',  False, False, False),
    # Sizzling Javalog Special
    ('Sizzling Javalog Special', 130, 'Sizzling Javalog Special', False, False, False),
    # Coffee
    ('Belgian Chocolate',        80,  'Coffee',                   False, True,  True),
    ('Cafe Americano',           80,  'Coffee',                   False, True,  True),
    ('Cafe Latte',               75,  'Coffee',                   False, True,  True),
    ('Cafe Mocha',               80,  'Coffee',                   False, True,  True),
    ('Cappuccino',               75,  'Coffee',                   False, True,  True),
    ('Caramel Macchiato',        80,  'Coffee',                   False, True,  True),
    ('Choco Hazelnut',           80,  'Coffee',                   False, True,  True),
    ('Mocha Caramel',            80,  'Coffee',                   False, True,  True),
    ('Roasted Almond',           80,  'Coffee',                   False, True,  True),
    ('Spanish Latte',            80,  'Coffee',                   False, True,  True),
    ('Vanilla',                  85,  'Coffee',                   False, True,  True),
    ('Vietnamese Coffee',        75,  'Coffee',                   False, True,  True),
    ('Bac Xiu Da',               75,  'Coffee',                   False, True,  True),
    ('Cafe Sua Da',              75,  'Coffee',                   False, True,  True),
    # Blended Drinks
    ('Butterscotch',             75,  'Blended Drinks',           False, True,  False),
    ('Double Choco Macchiato',   75,  'Blended Drinks',           False, True,  False),
    ('Macha Caramel',            75,  'Blended Drinks',           False, True,  False),
    ('Mocha Frappe',             75,  'Blended Drinks',           False, True,  False),
    ('Caramel Marshmallow',      75,  'Blended Drinks',           False, True,  False),
    ('Roasted Choco Hazelnut',   75,  'Blended Drinks',           False, True,  False),
    ('Salted Caramel Macchiato', 75,  'Blended Drinks',           False, True,  False),
    # Non-Coffee
    ('Caramel Macadamia Praline',75,  'Non-Coffee',               False, True,  False),
    ('Choco Berry Foam',         75,  'Non-Coffee',               False, True,  False),
    ('Dark Chocolate Almond',    75,  'Non-Coffee',               False, True,  False),
    ('Strawberry Cream',         75,  'Non-Coffee',               False, True,  False),
    # Milk Tea
    ('Belgian Chocolate MT',     75,  'Milk Tea',                 False, True,  False),
    ('Butterball',               75,  'Milk Tea',                 False, True,  False),
    ('Cheesecake',               75,  'Milk Tea',                 False, True,  False),
    ('Choco Hazelnut MT',        75,  'Milk Tea',                 False, True,  False),
    ('Salted Caramel',           75,  'Milk Tea',                 False, True,  False),
    # Refreshing
    ('Green Apple Cider',        75,  'Refreshing',               False, False, False),
    ('Green Apple Mojito',       75,  'Refreshing',               False, False, False),
    ('Lychee Cider',             75,  'Refreshing',               False, False, False),
    ('Passion Fruit Cider',      75,  'Refreshing',               False, False, False),
    ('Strawberry Mojito',        75,  'Refreshing',               False, False, False),
    # Hot Tea
    ('Black Tea',                55,  'Hot Tea',                  False, False, False),
    ('Jasmine',                  55,  'Hot Tea',                  False, False, False),
    ('Peppermint',               55,  'Hot Tea',                  False, False, False),
    # Add Ons
    ('Coffee Jelly',             40,  'Add Ons',                  False, False, False),
    ('Popping Pearl',            40,  'Add Ons',                  False, False, False),
]

created = 0
for name, price, cat, has_serving, has_size, has_temp in menu_items:
    if not MenuItem.objects.filter(name=name).exists():
        MenuItem.objects.create(
            name=name, price=price, category=cat,
            has_serving_style=has_serving,
            has_size=has_size,
            has_temperature=has_temp,
        )
        created += 1
print(f"  Created {created} menu items")

# ── Inventory ──────────────────────────────────────────
inventory_items = [
    ('Beef (kg)',        46, 'kg',   20),
    ('Milk (L)',         82, 'L',    15),
    ('Coffee Beans (kg)', 4, 'kg',  15),
    ('Pork (kg)',        30, 'kg',   10),
    ('Chicken (kg)',     25, 'kg',   10),
    ('Rice (kg)',        50, 'kg',   20),
    ('Cooking Oil (L)',  10, 'L',     5),
    ('Sugar (kg)',       15, 'kg',    5),
    ('Cheese (kg)',       8, 'kg',    3),
    ('Flour (kg)',       20, 'kg',    8),
]
inv_created = 0
for name, stock, unit, min_level in inventory_items:
    if not InventoryItem.objects.filter(name=name).exists():
        InventoryItem.objects.create(name=name, stock=stock, unit=unit, min_level=min_level)
        inv_created += 1
print(f"  Created {inv_created} inventory items")

print("\n✅ Setup complete!")
print("\nDefault Login Credentials:")
print("  Admin:   admin / admin123")
print("  Cashier: cashier / cashier123")
print("  Kitchen: kitchen / kitchen123")
print("\nRun the server:")
print("  python manage.py runserver")
print("  Then open: http://127.0.0.1:8000")
