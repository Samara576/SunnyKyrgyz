from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


class CustomTokenAuthentication(TokenAuthentication):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            raise AuthenticationFailed('You must be authenticated to access this resource.')

        return True


class IsUnregistered(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return not request.user.is_authenticated


class IsClient(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.user_type == 'client'


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.user_type == 'owner'


class IsAdminUser(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.is_staff


class IsOwnerAndClient(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return request.user.is_authenticated and request.user.user_type == "owner" or "client"
