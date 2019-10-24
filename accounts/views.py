from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.views.generic import FormView

from .forms import LoginForm, RegisterForm


class LoginFormView(FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm

    def get_success_url(self):
        return self.request.GET.get('next') or self.request.POST.get('next') or '/'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)


class RegisterFormView(FormView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = '/accounts/login'

    def form_valid(self, form):
        form.register_user()
        return super().form_valid(form)


def logout_page(request):
    logout(request)
    return redirect('login')
