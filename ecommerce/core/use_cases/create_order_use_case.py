# ecommerce/core/use_cases/create_order_use_case.py
from ecommerce.core.entities.order import Order
from ecommerce.core.repositories.product_repository import ProductRepository
from ecommerce.core.repositories.user_repository import UserRepository

class CreateOrderUseCase:
    def __init__(self, user_repository: UserRepository, product_repository: ProductRepository):
        self.user_repository = user_repository
        self.product_repository = product_repository

    def execute(self, user_id, product_ids):
        user = self.user_repository.get_by_id(user_id)
        products = [self.product_repository.get_by_id(product_id) for product_id in product_ids]

        order = Order.objects.create(user=user)
        order.products.set(products)

        return order
