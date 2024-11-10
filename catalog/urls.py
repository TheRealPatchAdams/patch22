# catalog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('catalog/', views.catalog, name='catalog'),
    path('add-product/', views.add_product, name='add_product'),
    path('coupons/', views.active_coupons, name='active_coupons'),
]
