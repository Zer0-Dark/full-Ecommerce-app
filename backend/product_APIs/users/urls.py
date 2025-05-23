from django.urls import path
from .views import LoginAPIView, RegistrationAPIView, LogoutAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name="login"),
    path('register/', RegistrationAPIView.as_view(), name="register"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
]
