from rest_framework import permissions
from .models import Book


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff and request.user


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if obj.__class__ == Book:
            return request.user == obj.author.user
        return request.user == obj.user
