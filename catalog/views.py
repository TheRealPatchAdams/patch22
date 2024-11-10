# catalog/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  # Import CSRF exemption decorator
from django.views.decorators.http import require_http_methods
from .models import Product, Coupon

# Endpoint to get all products
@require_http_methods(["GET"])
def catalog(request):
    """Fetches and returns a list of all products in JSON format."""
    products = list(Product.objects.values())
    return JsonResponse(products, safe=False)

# Endpoint to add a new product (example for POST request)
@csrf_exempt  # Disables CSRF protection for this view
@require_http_methods(["POST"])
def add_product(request):
    """Adds a new product to the catalog based on POST data."""
    name = request.POST.get('name')
    description = request.POST.get('description', '')
    price = request.POST.get('price')
    stock = request.POST.get('stock', 0)

    # Create a new product in the database
    product = Product.objects.create(
        name=name,
        description=description,
        price=price,
        stock=stock
    )
    return JsonResponse({'message': 'Product added successfully', 'product_id': product.id})

# Endpoint to get all active coupons
@require_http_methods(["GET"])
def active_coupons(request):
    """Fetches and returns a list of all active coupons in JSON format."""
    coupons = list(Coupon.objects.filter(active=True).values())
    return JsonResponse(coupons, safe=False)
