from django.urls import path

from .views import MeView

app_name = "myauth"

urlpatterns = [
    path('me', MeView.as_view(), name="me"),
]