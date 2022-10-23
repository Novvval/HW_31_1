from rest_framework import permissions
from ads.models import User, Ad, Selection


class AdPermission(permissions.BasePermission):
    message = "Not authorized"

    def has_permission(self, request, view):
        if request.user.role != User.Role.MEMBER:
            return True
        elif request.user.id == Ad.author:
            return True
        return False


class SelectionPermission(permissions.BasePermission):
    message = "not authorized"

    def has_permission(self, request, view):
        if request.user.role != User.Role.MEMBER:
            return True
        elif request.user.id == Selection.owner:
            return True
        return False
