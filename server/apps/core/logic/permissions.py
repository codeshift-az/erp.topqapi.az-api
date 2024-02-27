from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminUserOrReadOnlyForStaff(BasePermission):
    """Allow access to admin users and read-only for staff."""

    def has_permission(self, request, view):
        """Check if user has permission."""

        if not request.user.is_authenticated:
            return False

        if not request.user.is_staff:
            return False

        if not request.user.is_superuser:
            return request.method in SAFE_METHODS

        return True
