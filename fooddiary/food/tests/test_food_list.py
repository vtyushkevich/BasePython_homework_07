from http import HTTPStatus

from django.template.response import TemplateResponse
from django.test import TestCase
from django.urls import reverse_lazy, reverse

from food.models import FoodItem


class FoodListTestCase(TestCase):
    fixtures = [
        "food_meal.fix.json",
        "food_kind.fix.json",
        "fooditem.fix.json",
    ]

    url = reverse_lazy("food:index")

    def test_list_food(self):
        url = reverse("food:index")
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        food = (
            FoodItem
            .objects
            .select_related("kind")
            .prefetch_related("meal")
            .order_by("pk")
            .all()
        )
        food_in_context = response.context["foodlist"]
        self.assertEqual(len(food), len(food_in_context))
        for a1, a2 in zip(food, food_in_context):
            self.assertEqual(a1.pk, a2.pk)

    def test_anon_access(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(response.context["user"].is_anonymous)
