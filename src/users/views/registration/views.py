from django.views.generic import FormView

from src.users.form.user import UserForm
from src.users.services.auth import AuthService


class RegistrationView(FormView):
    template_name = 'registration/registration.html'
    form_class = UserForm
    success_url = '/'

    def form_valid(self, form):
        AuthService.register(self.request,
                             username=form.cleaned_data['username'],
                             password=form.cleaned_data['password2'])
        return super().form_valid(form)
