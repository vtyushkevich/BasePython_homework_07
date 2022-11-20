from typing import TYPE_CHECKING

from django.contrib import admin

from .models import FoodItem, FoodProfile, FoodKind, FoodTypeMeal

if TYPE_CHECKING:
    admin.site: admin.AdminSite


class FoodAdmin(admin.ModelAdmin):
    list_display = "name", "manufacturer", "calory"


admin.site.register(FoodItem, FoodAdmin)


@admin.register(FoodProfile)
class FoodProfileAdmin(admin.ModelAdmin):
    list_display = "pk", "origin"


@admin.register(FoodKind)
class FoodKindAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "desc"


@admin.register(FoodTypeMeal)
class FoodTypeMealAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "desc"