from django.urls import path

from src.users.views.account.views import AccountView, AccountUpdateView
from src.users.views.login.views import LoginView
from src.users.views.logout.views import LogoutView
# from src.users.views.registration.views import CreateUserView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    # path('registration', CreateUserView().as_view(), name='registration'),
    # path('password/change', , name='password_change'),
    # path('password/reset', , name='password_reset'),
    # path('reset/<int:uidb64>/<str:token>', , name='password_reset_confirm'),
    path('account/get/<str:slug>', AccountView().as_view(), name='get-account'),
    path('account/update', AccountUpdateView().as_view(), name='update-account'),
]
