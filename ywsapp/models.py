from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


class VoiceActing(models.IntegerChoices):
    FULL = 0, 'Full'
    NO_COMMENTS = 1, 'No comments'
    ASANA_START_STOP = 2, 'Asana start/stop'
    ASANA_START_ONLY = 3, 'Asana start only'

# Create your models here.
class User(AbstractUser):
    complete_workouts = models.PositiveIntegerField(default=0)
    last_workout_id = models.TextField(default="-")
    last_workout_date = models.DateTimeField(default=datetime.now)
    kegel_timer = models.BooleanField(default=False)
    voice_acting = models.IntegerField(default=VoiceActing.FULL, choices=VoiceActing.choices)

class UserWorkoutProps(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prop_id = models.CharField(max_length=120)
    value = models.IntegerField()
