from rest_framework import serializers
from crm.models import User, Client, Contract, Event


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id',
                  'first_name',
                  'last_name',
                  'email',
                  'password',
                  'role',
                  )

        extra_kwargs = {'password': {'write_only': True}}


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ["id",
                  "first_name",
                  "last_name",
                  "email",
                  "phone",
                  "mobile",
                  "company_name",
                  "date_created",
                  "date_updated",
                  "sales_contact",
                  "status"
                  ]


class ContractSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contract
        fields = ["id",
                  "client",
                  "date_created",
                  "date_signed",
                  "date_updated",
                  "amount",
                  "status"
                  ]


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ["id",
                  "name",
                  "contract",
                  "start_date",
                  "end_date",
                  "support_contact",
                  "notes",
                  "status"
                  ]
