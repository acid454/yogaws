from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


class VoiceActing(models.IntegerChoices):
    FULL = 0, 'Full'
    NO_COMMON_COMMENTS = 1, 'No common comments'
    NO_ANY_COMMENTS = 2, 'No any comments'
    ASANA_START_STOP = 3, 'Asana start and stop only'
    ASANA_START_ONLY = 4, 'Asana start only'

class ShavasanaActing(models.IntegerChoices):
    SETTINGS_DEPEND = 0, 'Depends on settings'
    ALWAYS_ACTING = 1, 'Acting always'
    NEVER_ACTING = 2, 'Never acting'

class MetronomeTicks(models.IntegerChoices):
    FULL = 0, 'Full'
    ONLY_BELLS = 1, 'Bells only'
    NONE = 2, 'No metronome sound'

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
