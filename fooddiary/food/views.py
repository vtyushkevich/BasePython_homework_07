from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import FoodItem


def index(request: HttpRequest):

    # return HttpResponse(f"<h1>Hello path <code>{request.path}</code><h1>")
    context = {
        "food": FoodItem.objects.order_by("pk").all()
    }
    return render(request=request, template_name="food/index.html", context=context)


def details(request: HttpRequest, pk: int):
    context = {
        "food": get_object_or_404(FoodItem, pk=pk)
    }
    return render(request=request, template_name="food/details.html", context=context)