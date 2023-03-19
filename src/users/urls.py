from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from src.users.views.registration.views import RegistrationView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('registration', RegistrationView.as_view(), name='registration'),
]
