from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend

CustomUser = get_user_model()


class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = CustomUser.objects.get(email=email)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None
