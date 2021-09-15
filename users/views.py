from django.contrib.auth import get_user_model, login
from django.http import HttpResponse
from django.views import View
from django.views.generic import FormView, ListView
from users.forms import RegistrationForm, LoginForm

User = get_user_model


class RegisterView(FormView):
    form_class = RegistrationForm
    template_name = "register.html"
    success_url = ""

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(FormView):
    form_class = LoginForm
    template_name = "login.html"
    success_url = ""

    def form_valid(self, form):
        login(self.request, self.get_context_data(['user']))
        return super().form_valid(form)


class LogOut(ListView):
    success_url = ""
