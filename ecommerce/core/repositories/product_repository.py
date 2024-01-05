# ecommerce/core/repositories/product_repository.py
from ecommerce.core.entities.product import Product

class ProductRepository:
    def get_by_id(self, product_id):
        return Product.objects.get(pk=product_id)

    def create(self, product):
        return Product.objects.create(
            name=product.name,
            price=product.price,
        )
