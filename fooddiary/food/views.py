from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import FoodItem


def index(request: HttpRequest):

    # return HttpResponse(f"<h1>Hello path <code>{request.path}</code><h1>")
    context = {
        "food": FoodItem.objects.select_related("kind").order_by("kind").all()
    }
    return render(request=request, template_name="food/index.html", context=context)


class FoodListView(ListView):
    # model = FoodItem
    context_object_name = "foodlist"
    queryset = (
        FoodItem
        .objects
        .select_related("kind")
        .order_by("pk")
        .all()
    )


class FoodDetailView(DetailView):
    template_name = "food/details.html"
    context_object_name = "food"
    queryset = (
        FoodItem.objects.select_related("profile", "kind")
    )


def details(request: HttpRequest, pk: int):
    context = {
        "food": get_object_or_404(
            FoodItem.objects.select_related("profile", "kind"),
            pk=pk
        )
    }
    return render(request=request, template_name="food/details.html", context=context)