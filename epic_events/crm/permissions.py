from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsManagement(BasePermission):
    """Grants full access to Management team."""

    def has_object_permission(self, request, view, obj):
        if request.user.role == 'MANAGEMENT':
            return True
        return False


class IsClientSalesContactOrReadOnly(BasePermission):
    """
    Permissions:
    - Sales: Can create and manage clients they are assigned to.
    - Support: Read-only access.
    """

    message = "Only the sales contact assigned to the client can add or update."

    def has_permission(self, request, view):
        if request.method == 'POST' and request.user.role == 'SUPPORT':
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.sales_contact == request.user


class IsContractSalesContactOrReadOnly(BasePermission):
    """
    Permissions:
    - Sales: Can create and manage contracts of clients they are assigned to.
    - Support: Read-only access.
    """
    message = "Only sales users assigned to the client of the contract can add and update."

    def has_permission(self, request, view):
        if request.method == 'POST' and request.user.role == 'SUPPORT':
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.client.sales_contact == request.user


class IsEventSalesOrSupportContact(BasePermission):
    """
    Permissions:
    - Sales: Can create and manage contracts of clients they are assigned to.
    - Support: Read-only on all events, and edit rights for assigned events.
    """
    message = "Only sales users assigned to the client of the event can add. " \
              "And Update allowed only for the event's sales and support contacts."

    def has_permission(self, request, view):
        if request.method == 'POST' and request.user.role == 'SUPPORT':
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.contract.client.sales_contact == request.user or obj.support_contact == request.user


class UserPermission(BasePermission):
    """
      Object-level permission to only allow users to update their own account.
    """
    message = "You can only access and update your own account."

    def has_object_permission(self, request, view, obj):

        if view.action in ["retrieve", "update", "partial_update"]:
            return (
                    obj == request.user
            )  # Allow the user to retrieve, update or partial_update their own data
        else:
            return False  # For other actions, deny all requests
