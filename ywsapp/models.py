from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
import os, sys
base_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(base_dir, "yoga/containers"))
from integer_constants import VoiceActing, ShavasanaActing, MetronomeTicks


# Create your models here.
class User(AbstractUser):
    complete_workouts = models.PositiveIntegerField(default=0)
    last_workout_id = models.TextField(default="-")
    last_workout_date = models.DateTimeField(default=datetime.now)
    kegel_timer = models.BooleanField(default=False)
    voice_acting = models.IntegerField(default=VoiceActing.FULL, choices=VoiceActing.choices)
    shavasana_acting = models.IntegerField(default=ShavasanaActing.SETTINGS_DEPEND, choices=ShavasanaActing.choices)
    metronome = models.IntegerField(default=MetronomeTicks.FULL, choices=MetronomeTicks.choices)

class UserWorkoutProps(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prop_id = models.CharField(max_length=120)
    value = models.IntegerField()
