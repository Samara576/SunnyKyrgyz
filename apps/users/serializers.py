from rest_framework.authtoken.models import Token
from rest_framework import serializers

from .validators import validate_email, validate_password
from .models import CustomUser, ReviewSite, Profile


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "email", "username", "user_type", "date_of_birth", "is_staff", "verify_code", "is_active")


class SignUpSerializer(serializers.ModelSerializer):
    def validate_password(self, value):
        return validate_password(value)

    def validate_email(self, value):
        queryset = CustomUser.objects.all()
        return validate_email(value, queryset)

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.get_or_create(user=user)
        return user

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'user_type', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class VerifySerializer(serializers.Serializer):
    email = serializers.EmailField()
    verify_code = serializers.CharField()


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    access_token = serializers.CharField(read_only=True)
    refresh_token = serializers.CharField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'refresh_token', 'access_token']
        extra_kwargs = {'password': {'write_only': True},
                        'refresh_token': {'read_only': True},
                        'access_token': {'read_only': True}}


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class PasswordResetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        style={"input_type": "password"}, help_text="From 6 to 20", min_length=6
    )


class PasswordResetCodeSerializer(serializers.Serializer):
    code = serializers.CharField()


class PasswordResetSearchUserSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        fields = ['email']


class ReviewSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewSite
        fields = ('id', 'user', 'content', 'created_at')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'image', 'email', 'phone_number']
        read_only_fields = ['email']