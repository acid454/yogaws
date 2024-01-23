from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

# Create your models here.
class User(AbstractUser):
    complete_workouts = models.PositiveIntegerField(default=0)
    last_workout_id = models.TextField(default="-")
    last_workout_date = models.DateTimeField(default=datetime.now)

class UserWorkoutProps(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prop_id = models.CharField(max_length=120)
    value = models.IntegerField()
