# ecommerce/interfaces/web/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User as DjangoUser
from ecommerce.core.use_cases.create_order_use_case import CreateOrderUseCase
from ecommerce.core.repositories.product_repository import ProductRepository
from ecommerce.core.repositories.user_repository import UserRepository
from ecommerce.core.use_cases.create_product_use_case import CreateProductUseCase
from django.contrib.auth.hashers import make_password
import json

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            username = data.get('username')
            email = data.get('email')
            password = data.get('password')
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        # Validate that required fields are present
        if not username or not email or not password:
            return JsonResponse({'error': 'Missing required fields'}, status=400)

        # Create Django User
        django_user = DjangoUser.objects.create(
            username=username,
            email=email,
            password=make_password(password)
        )

        # Create Custom User (assuming you have a custom User model)
        user_repository = UserRepository()
        custom_user = user_repository.create_user(django_user.id, username, email)

        return JsonResponse({
            'user_id': custom_user.id,
            'username': custom_user.username,
            'email': custom_user.email,
        })

    # Handle other HTTP methods
    return JsonResponse({'error': 'Invalid HTTP method'}, status=400)

@csrf_exempt
def create_product(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            name = data.get('name')
            price = data.get('price')
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        # Validate that required fields are present
        if not name or not price:
            return JsonResponse({'error': 'Missing required fields'}, status=400)

        product_repository = ProductRepository()
        create_product_use_case = CreateProductUseCase(product_repository)

        product = create_product_use_case.execute(name, price)

        return JsonResponse({
            'product_id': product.id,
            'name': product.name,
            'price': product.price,
        })

    # Handle other HTTP methods
    return JsonResponse({'error': 'Invalid HTTP method'}, status=400)

@csrf_exempt
def create_order(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            user_id = data.get('user_id')
            product_ids = data.get('product_ids', [])
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)

        # Validate that required fields are present
        if not user_id or not product_ids:
            return JsonResponse({'error': 'Missing required fields'}, status=400)

        user_repository = UserRepository()
        product_repository = ProductRepository()
        create_order_use_case = CreateOrderUseCase(user_repository, product_repository)

        order = create_order_use_case.execute(user_id, product_ids)

        return JsonResponse({
            'order_id': order.id,
            'user_id': order.user.id,
            'product_ids': [product.id for product in order.products.all()],
        })

    # Handle other HTTP methods
    return JsonResponse({'error': 'Invalid HTTP method'}, status=400)
