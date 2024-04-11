from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import RegisterView, GetMeAPIView

urlpatterns = [
    # JWT Urls
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Auth
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('getMe/', GetMeAPIView.as_view(), name='get-me'),
]
