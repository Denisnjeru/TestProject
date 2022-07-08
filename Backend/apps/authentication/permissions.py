from rest_framework import permissions
from  rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAuthenticated, BasePermission, DjangoModelPermissions
from django.contrib.auth.models import Permission
from .models  import Profile
from .models import *

class IsOwner(BasePermission):
    message = "Not the owner"

    def has_object_permission(self, request, view, obj):
        return request.user ==  obj.user


class IsClient(BasePermission):
    message = "Not Client"

    def has_permission(self, request, view):
        return bool(request.user.user_type == 'client')

class IsSupplier(BasePermission):
    message = "Not Supplier"

    def has_permission(self, request, view):
        return bool(request.user.user_type == 'supplier')

class IsEprocureAdmin(BasePermission):
    message = 'Not Eprocure Admin'

    def has_permission(self, request, view):
        return bool(request.user.user_type == 'eprocure-admin')
