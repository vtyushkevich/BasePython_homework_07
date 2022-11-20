from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import FoodItem


def index(request: HttpRequest):

    # return HttpResponse(f"<h1>Hello path <code>{request.path}</code><h1>")
    context = {
        "food": FoodItem.objects.select_related("kind").order_by("kind").all()
    }
    return render(request=request, template_name="food/index.html", context=context)


def details(request: HttpRequest, pk: int):
    context = {
        "food": get_object_or_404(
            FoodItem.objects.select_related("profile", "kind"),
            pk=pk
        )
    }
    return render(request=request, template_name="food/details.html", context=context)