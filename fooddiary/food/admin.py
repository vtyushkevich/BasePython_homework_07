from typing import TYPE_CHECKING

from django.contrib import admin

from .models import FoodItem

if TYPE_CHECKING:
    admin.site: admin.AdminSite


class FoodAdmin(admin.ModelAdmin):
    list_display = "name", "manufacturer", "calory"


admin.site.register(FoodItem, FoodAdmin)