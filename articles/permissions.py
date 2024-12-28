from rest_framework import permissions
from rest_framework.views import View, Request
from rest_framework_simplejwt.authentication import JWTAuthentication


class ArticlesPermission(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return request.user.is_superuser or request.method in permissions.SAFE_METHODS



class ConditionalJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        if request.method in permissions.SAFE_METHODS:
            return None
        return super().authenticate(request)