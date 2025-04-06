from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from .manager import CustomUserManager
from .constants import *
from apps.travel.service import compress_image


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=45)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    date_of_birth = models.DateField(null=True)
    is_staff = models.BooleanField(default=False)
    verify_code = models.CharField(max_length=6, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'user_type']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email


class PasswordResetToken(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=100)
    time = models.DateTimeField()


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/avatars/', blank=True, null=True, verbose_name='Profiles_avatar')
    email = models.EmailField(verbose_name='Email')
    phone_number = PhoneNumberField(null=True, blank=True, verbose_name='Номер телефона')

    def save(self, *args, **kwargs):
        if self.user.email:
            self.email = self.user.email
        super(Profile, self).save(*args, **kwargs)
        compress_image(self)

    def compress_image(self):
        return compress_image(self)

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'



class ReviewSite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return str(self.user)
