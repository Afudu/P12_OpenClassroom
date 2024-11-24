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
