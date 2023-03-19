from django.urls import path

from src.users.api_views.account.views import AccountView, AccountUpdateView
from src.users.api_views.login.views import LoginView
from src.users.api_views.logout.views import LogoutView
from src.users.api_views.registration.views import CreateUserView

urlpatterns = [
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('registration', CreateUserView().as_view()),
    path('account/get/<str:slug>', AccountView().as_view(), name='get-account'),
    path('account/update/<str:slug>', AccountUpdateView().as_view(), name='update-account'),
]
