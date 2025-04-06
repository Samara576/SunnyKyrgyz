from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status, request
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.serializers import ChangePasswordSerializer
from apps.users.tokens import create_jwt_pair_for_user


def login_user(serializer):
    user = authenticate(
        email=serializer.validated_data["email"],
        password=serializer.validated_data["password"]
    )

    if user is not None:
        tokens = create_jwt_pair_for_user(user)
        response = {"message": "Login Successful", "tokens": tokens}
        return Response(data=response, status=status.HTTP_200_OK)
    else:
        return Response(
            data={"message": "Invalid email or password"},
            status=status.HTTP_401_UNAUTHORIZED
        )
def refresh_access_token(self, request):
    try:
        refresh_token = request.data.get('refresh')
        refresh_token = RefreshToken(refresh_token)
        access_token = str(refresh_token.access_token)

        return Response({'access': access_token}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': 'Невозможно обновить токен'}, status=status.HTTP_400_BAD_REQUEST)