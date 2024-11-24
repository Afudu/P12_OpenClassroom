import django_filters
from .models import Client, Contract, Event


class ClientFilter(django_filters.FilterSet):
    class Meta:
        model = Client
        fields = ['company_name', 'email', 'sales_contact']


class ContractFilter(django_filters.FilterSet):
    class Meta:
        model = Contract
        fields = ['client', 'amount', 'status']


class EventFilter(django_filters.FilterSet):
    class Meta:
        model = Event
        fields = ['contract', 'support_contact', 'status']
