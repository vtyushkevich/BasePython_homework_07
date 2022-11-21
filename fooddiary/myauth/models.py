from typing import TYPE_CHECKING

from django.contrib.auth import get_user_model
from django.db import models

from django.contrib.auth.models import AbstractUser

UserModel: AbstractUser = get_user_model()

# class UserDetails(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
# class MyCustomUser(AbstractUser):
#     bio = models.TextField(blank=True)


class UserProfile(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True)

    if TYPE_CHECKING:
        objects: models.Manager
