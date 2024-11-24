from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from crm.models import User, Client, Contract, Event
from crm.serializers import UserSerializer, ClientSerializer, ContractSerializer, EventSerializer
from crm.permissions import IsManagement, IsClientSalesContactOrReadOnly, IsContractSalesContactOrReadOnly, \
    IsEventSalesOrSupportContact
from crm.filters import ClientFilter, ContractFilter, EventFilter


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsManagement]

    def get_queryset(self):
        """
        This view should return a list of users based on the queryset.
        """
        # Users list ordered by date joined.
        return User.objects.all().order_by("date_joined")


class ClientViewSet(ModelViewSet):
    """
    ViewSet for managing clients.
    """
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClientFilter
    permission_classes = [IsAuthenticated, IsClientSalesContactOrReadOnly]

    def get_queryset(self):
        # use order_by to avoid the warning for the pagination
        return Client.objects.all().order_by("date_created")

    def perform_create(self, serializer):
        """
        Creation of a model instance.
        """
        # upon creation, the logged-in user is saved as sales_contact.
        serializer.save(sales_contact=self.request.user)


class ContractViewSet(ModelViewSet):
    """
    ViewSet for managing contracts.
    """
    serializer_class = ContractSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ContractFilter
    permission_classes = [IsAuthenticated, IsContractSalesContactOrReadOnly]

    def get_queryset(self):
        # use order_by to avoid the warning for the pagination
        return Contract.objects.all().order_by("date_created")


class EventViewSet(ModelViewSet):
    """
    ViewSet for managing events.
    """
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EventFilter
    permission_classes = [IsAuthenticated, IsEventSalesOrSupportContact]

    def get_queryset(self):
        # use order_by to avoid the warning for the pagination
        return Event.objects.all().order_by("date_created")
