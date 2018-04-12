from django.db import models
from django.utils import timezone


# Create your models here.
class Exercise(models.Model):
    id = models.AutoField(primary_key=True)
    exercise_date = models.DateField(auto_created=True)
    exercise = models.CharField(max_length=255, blank=False, default='')
    weight = models.CharField(max_length=255, blank=True, default='')
    reps = models.CharField(max_length=255, blank=True, default='')
    sets = models.CharField(max_length=255, blank=True, default='')

    def __str__(self):
        return self.exercise
