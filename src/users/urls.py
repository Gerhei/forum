from django.urls import path

from src.users.views.login.views import LoginView
from src.users.views.logout.views import LogoutView

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    # path('password/change', , name='password_change'),
    # path('password/reset', , name='password_reset'),
    # path('reset/<int:uidb64>/<str:token>', , name='password_reset_confirm'),
]
