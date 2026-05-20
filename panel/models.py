from django.db import models


CATEGORY_CHOICES = [
    ('Sizzling Steaks', 'Sizzling Steaks'),
    ('Burger With Fries', 'Burger With Fries'),
    ('Appetizer', 'Appetizer'),
    ('Pasta', 'Pasta'),
    ('Grilled Rice Meals', 'Grilled Rice Meals'),
    ('Sizzling Javalog 99ers', 'Sizzling Javalog 99ers'),
    ('Sizzling Javalog Special', 'Sizzling Javalog Special'),
    ('Brewsko Special', 'Brewsko Special'),
    ('Wings With Fries', 'Wings With Fries'),
    ('The Ultimate Sisig', 'The Ultimate Sisig'),
    ('Pizza', 'Pizza'),
    ('Coffee', 'Coffee'),
    ('Blended Drinks', 'Blended Drinks'),
    ('Non-Coffee', 'Non-Coffee'),
    ('Milk Tea', 'Milk Tea'),
    ('Refreshing', 'Refreshing'),
    ('Hot Tea', 'Hot Tea'),
    ('Add Ons', 'Add Ons'),
]

FOOD_CATEGORIES = [
    'Sizzling Steaks', 'Burger With Fries', 'Appetizer', 'Pasta',
    'Grilled Rice Meals', 'Sizzling Javalog 99ers', 'Sizzling Javalog Special',
    'Brewsko Special', 'Wings With Fries', 'The Ultimate Sisig', 'Pizza',
]

DRINK_CATEGORIES = [
    'Coffee', 'Blended Drinks', 'Non-Coffee', 'Milk Tea',
    'Refreshing', 'Hot Tea', 'Add Ons',
]


class MenuItem(models.Model):
    STATUS_CHOICES = [('available', 'Available'), ('unavailable', 'Unavailable')]
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    achieved = models.BooleanField(default=False)
    has_serving_style = models.BooleanField(default=False)
    has_size = models.BooleanField(default=False)
    has_temperature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - ₱{self.price}"

    @property
    def is_food(self):
        return self.category in FOOD_CATEGORIES

    @property
    def is_drink(self):
        return self.category in DRINK_CATEGORIES


class Addon(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    applies_to = models.CharField(max_length=20, choices=[('food', 'Food'), ('drink', 'Drink'), ('both', 'Both')], default='both')

    def __str__(self):
        return self.name


class InventoryItem(models.Model):
    UNIT_CHOICES = [('kg', 'kg'), ('L', 'L'), ('pcs', 'pcs'), ('pack', 'pack')]
    STATUS_CHOICES = [('good', 'Good'), ('low', 'Low Stock'), ('critical', 'Critical')]

    name = models.CharField(max_length=100)
    stock = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES, default='kg')
    min_level = models.DecimalField(max_digits=10, decimal_places=2)
    achieved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.stock}{self.unit})"

    @property
    def status(self):
        ratio = float(self.stock) / float(self.min_level) if self.min_level > 0 else 1
        if ratio <= 0.3:
            return 'critical'
        elif ratio <= 1.0:
            return 'low'
        return 'good'

    @property
    def status_label(self):
        return {'critical': 'Critical', 'low': 'Low Stock', 'good': 'Good'}[self.status]
