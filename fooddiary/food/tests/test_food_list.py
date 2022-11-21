from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse_lazy, reverse

from food.models import FoodItem


class FoodListTestCase(TestCase):
    # fixtures = [
    #     "animal_foods.fixture.json",
    #     "animal_kinds.fixture.json",
    #     "animals.fixture.json",
    # ]

    def test_list_food(self):
        url = reverse("food:index")
        response = self.client.get(url)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        # food = (
        #     FoodItem
        #     .objects
        #     .select_related("kind")
        #     .prefetch_related("meal")
        #     # .filter(archived=False)
        #     .order_by("pk")
        #     .all()
        # )
        # print(response.context)
        # food_in_context = response.context["food"]
        # self.assertEqual(len(food), len(food_in_context))
        # for a1, a2 in zip(food, food_in_context):
        #     self.assertEqual(a1.pk, a2.pk)

    # def test_anon_access(self):
    #     response = self.client.get(self.url)
    #     self.assertEqual(response.status_code, HTTPStatus.OK)
    #     self.assertTrue(response.context["user"].is_anonymous)
