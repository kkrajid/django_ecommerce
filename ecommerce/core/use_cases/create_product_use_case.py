
from ecommerce.core.entities.product import Product
from ecommerce.core.repositories.product_repository import ProductRepository

class CreateProductUseCase:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def execute(self, name, price):
        product = Product(id=None, name=name, price=price)
        return self.product_repository.create(product)
