from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsStaffOrReadOnly(BasePermission):
    message = "Only staff users may change student records."

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or bool(request.user and request.user.is_staff)


# NOTES ABOUT THE COMPLETE CODE ABOVE
# BasePermission is the extension point for an access rule.
# SAFE_METHODS contains GET, HEAD and OPTIONS; these should not change state.
# Anonymous and ordinary users can read. Only authenticated staff users can write.
# has_permission checks the whole request. has_object_permission would check one object.
# Object permissions do not automatically filter list querysets; use get_queryset for that.
# This permission still requires authentication to identify the staff user.
