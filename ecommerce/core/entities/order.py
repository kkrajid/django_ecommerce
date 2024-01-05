
from django.db import models
from .user import User
from .product import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f'Order-{self.id} by {self.user.username}'
