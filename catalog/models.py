# catalog/models.py
from django.contrib import admin 

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Additional fields for franchise data if needed

class Coupon(models.Model):
    code = models.CharField(max_length=50)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)  # Quantity available in stock
    image_url = models.URLField(blank=True, null=True)  # URL to product image
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)  # Unique discount code
    discount_percentage = models.IntegerField()  # Discount as a percentage
    active = models.BooleanField(default=True)  # If the coupon is currently active
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} - {self.discount_percentage}% off"

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.product.name} x {self.quantity}"
