from django.urls import path

from .views import MeView, LoginView

app_name = "myauth"

urlpatterns = [
    path('me', MeView.as_view(), name="me"),
    path("login/", LoginView.as_view(), name="login"),
]