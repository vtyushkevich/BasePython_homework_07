from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.views import (
    LoginView as LoginViewGeneric,
    LogoutView as LogoutViewGeneric,
)


class MeView(TemplateView):
    template_name = "myauth/me.html"


class LoginView(LoginViewGeneric):
    form_class = AuthenticationForm
    next_page = reverse_lazy("myauth:me")