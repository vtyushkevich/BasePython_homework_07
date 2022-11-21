from django.urls import path

from .views import index, details, FoodListView, FoodDetailView

app_name = "food"

urlpatterns = [
    # path('', index, name="index"),
    path('', FoodListView.as_view(), name="index"),
    # path('', FoodDetailView.as_view(), name="index"),
    path('<int:pk>', FoodDetailView.as_view(), name="details"),
    # path('<int:pk>', details, name="details"),
]