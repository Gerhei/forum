from rest_framework import permissions
from rest_framework.request import Request


class IsOwnerOrReadOnly(permissions.BasePermission):
    message = 'This can\'t be edited because you are not it is owner.'

    def has_object_permission(self, request: Request, view, obj) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
