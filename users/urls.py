from django.urls import path
from users.apps import UsersConfig
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from users.views import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView

app_name = UsersConfig.name

urlpatterns = [
    # users
    path('', UserListCreateAPIView.as_view(), name='list_create_user'),
    path('<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='retrieve_update_destroy_user'),

    # token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')

]