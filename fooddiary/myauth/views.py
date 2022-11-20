from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import TemplateView


class MeView(TemplateView):
    template_name = "myauth/me.html"