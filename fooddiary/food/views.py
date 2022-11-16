from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest):

    return HttpResponse(f"<h1>Hello path <code>{request.path}</code><h1>")