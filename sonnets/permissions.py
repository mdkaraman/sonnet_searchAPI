from rest_framework import permissions


class ObjectLevelIsAuthenticatedOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authenticated users to edit sonnets.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to authenticated users.
        return request.user.is_authenticated
