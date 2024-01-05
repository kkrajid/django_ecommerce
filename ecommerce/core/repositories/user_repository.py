# ecommerce/core/repositories/user_repository.py
from ecommerce.core.entities.user import User

class UserRepository:
    def get_by_id(self, user_id):
        return User.objects.get(pk=user_id)

    def create_user(self, django_user_id, username, email):
        return User.objects.create(
            id=django_user_id,
            username=username,
            email=email,
        )
