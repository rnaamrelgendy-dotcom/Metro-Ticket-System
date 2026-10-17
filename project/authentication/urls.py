from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView
from .views import UserListCreate

urlpatterns = [
    path('token/' , TokenObtainPairView.as_view() , name='token_obtain_pair'),
    path('token/refresh/' , TokenRefreshView.as_view() , name='token_refresh'),
    path('user/' , UserListCreate.as_view() , name='user_create')
] 