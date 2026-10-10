from django.db import models
from django.contrib.auth.models import User

class MealRecordModel(models.Model):

    title = models.CharField(max_length=200)

    calorie = models.PositiveIntegerField()

    MEAL_TYPE_OPTION = [

        ("BREAKFAST","BreakFast"),
        ("LUNCH","Lunch"),
        ("SNACK","Snack"),
        ("DINNER","Dinner"),
    ]

    meal_type = models.CharField(

        choices=MEAL_TYPE_OPTION,

        default="SNACK")

    serving_size = models.CharField(max_length=20)

    owner = models.ForeignKey(

        User,

        on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

      return self.title