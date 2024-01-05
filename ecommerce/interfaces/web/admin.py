
from django.contrib import admin
from ecommerce.core.entities.product import Product
from ecommerce.core.entities.user import User
from ecommerce.core.entities.order import Order

admin.site.register(Product)
admin.site.register(User)
admin.site.register(Order)
