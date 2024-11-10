# catalog/admin.py

from django.contrib import admin
from .models import Product, Coupon, Order

admin.site.register(Product)
admin.site.register(Coupon)
admin.site.register(Order)
