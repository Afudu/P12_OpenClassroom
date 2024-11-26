from django.urls import include, path
from rest_framework.routers import DefaultRouter
from crm.views import UserViewSet, ClientViewSet, ContractViewSet, EventViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = "crm"

# # DefaultRouter for the API Root
default_router = DefaultRouter()

# To generate:/users/ and /users/{pk}/
default_router.register(r'users', UserViewSet, basename='user')

# To generate /clients/ and /clients/{pk}/
default_router.register(r'clients', ClientViewSet, basename='client')

# To generate /contracts/ and /contracts/{pk}/
default_router.register(r'contracts', ContractViewSet, basename='contract')

# To generate /events/ and /events/{pk}/
default_router.register(r'events', EventViewSet, basename='event')

# # Wire up our API using automatic URL routing.
urlpatterns = [
    path('', include(default_router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
