from django.db import models


class FoodKind(models.Model):
    name = models.CharField(max_length=32)
    desc = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.name


class FoodTypeMeal(models.Model):
    class Meta:
        verbose_name_plural = "Meal"
    name = models.CharField(max_length=32)
    desc = models.TextField(blank=True, null=False)

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    name = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    unit = models.CharField(max_length=20)
    calory = models.PositiveIntegerField()
    fat_contents = models.PositiveIntegerField()
    carb_contents = models.PositiveIntegerField()
    protein_contents = models.PositiveIntegerField()
    kind = models.ForeignKey(FoodKind, on_delete=models.PROTECT, related_name="fooditem")
    meal = models.ManyToManyField("food.FoodTypeMeal", related_name="food")

    def __str__(self):
        return self.name


class FoodProfile(models.Model):
    food = models.OneToOneField(
        FoodItem,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    origin = models.CharField(max_length=64)

    def __str__(self):
        return f"Food {self.food.pk} from {self.origin}"


