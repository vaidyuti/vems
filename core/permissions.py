from rest_framework import permissions


class P2PTransaction(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated

        if view.action in ["update", "partial_update"]:
            return False

        if view.action == "destroy":
            return False

        return False

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated

        if view.action == "create":
            return False

        return True
