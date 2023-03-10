from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from .forms import LoginForm, RegistrationForm


class LoginUsersView(LoginView):
    template_name = 'service_users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('index')


class RegistrationView(CreateView):
    template_name = 'service_users/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')