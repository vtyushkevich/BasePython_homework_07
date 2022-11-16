from django.db import models


class FoodItem(models.Model):
    name = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    unit = models.CharField(max_length=20)
    calory = models.PositiveIntegerField()
    fat_contents = models.PositiveIntegerField()
    carb_contents = models.PositiveIntegerField()
    protein_contents = models.PositiveIntegerField()

    def __str__(self):
        return self.name