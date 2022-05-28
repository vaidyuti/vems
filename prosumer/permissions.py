from rest_framework import permissions


class Generation(permissions.IsAuthenticated):
    pass


class Load(permissions.IsAuthenticated):
    pass


class Prosumer(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return obj.user == request.user

        if view.action in ["update", "partial_update"]:
            return obj.user == request.user

        if view.action == "destroy":
            return request.user.is_authenticated and request.user.is_superuser

        return False

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated

        if view.action == "create":
            return request.user.is_authenticated

        return True


class Storage(permissions.IsAuthenticated):
    pass
