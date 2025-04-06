from django.contrib.auth import hashers
from rest_framework import status, response
from rest_framework.response import Response
from django.utils import timezone
from apps.users import models
from .emails import send_email_confirmation, send_email_reset_password
from .models import CustomUser, Profile
from .tokens import confirmation_code, recovery_code


class RegisterService:
    @staticmethod
    def create_user(serializer, request):
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        profile = Profile.objects.create(user=user)
        send_email_confirmation(user.email)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class VerifyService:
    @staticmethod
    def verify_code(serializer):
        serializer.is_valid(raise_exception=True)
        email = serializer.data['email']
        code = serializer.data['verify_code']

        user = CustomUser.objects.filter(email=email).first()
        if not user:
            return Response({'error': 'Неверный email.'}, status=400)

        if user.verify_code != code:
            return Response({'error': 'Неверный код подтверждения.'}, status=400)

        user.is_active = True
        user.save()

        return Response({'message': 'Аккаунт успешно подтвержден.'}, status=200)


class ResetPasswordSendEmail:

    @staticmethod
    def password_reset_email(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            email = serializer.validated_data["email"]
            user = models.CustomUser.objects.get(email=email)
        except:
            return response.Response(
                data={
                    "error": "Пользователь с указанным адресом электронной почты не найден."
                }
            )

        time = timezone.now() + timezone.timedelta(minutes=5)

        password_reset_token = models.PasswordResetToken(
            user=user, code=recovery_code, time=time
        )
        password_reset_token.save()

        send_email_reset_password(user.email)

        return response.Response(data={"detail": f'код для сброса пароля отправлен на вашу почту {user.email}'}, status=status.HTTP_200_OK)


class PasswordResetCode:
    @staticmethod
    def password_reset_code(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            code = serializer.validated_data["code"]
            reset_code = models.PasswordResetToken.objects.get(
                code=code, time__gt=timezone.now()
            )
        except Exception as e:
            return response.Response(
                status=status.HTTP_406_NOT_ACCEPTABLE,
                data={
                    "error": f"Недействительный код для сброса пароля или время истечения кода закончилось.{e}"},
            )
        return response.Response(
            data={"detail": "success", "code": f"{code}"}, status=status.HTTP_200_OK)


class PasswordResetNewPassword:
    @staticmethod
    def password_reset_new_password(code, password):
        try:
            password_reset_token = models.PasswordResetToken.objects.get(
                code=recovery_code, time__gt=timezone.now()
            )
        except models.PasswordResetToken.DoesNotExist:
            return False, "Недействительный код для сброса пароля или время истечения кода закончилось."

        user = password_reset_token.user
        user.password = hashers.make_password(password)
        user.save()

        password_reset_token.delete()
        return True, "Пароль успешно обновлен"
