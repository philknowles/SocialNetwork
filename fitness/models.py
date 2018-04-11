from django.db import models


# Create your models here.
class Exercise(models.Model):
    id = models.AutoField(primary_key=True)
    exercise = models.CharField(max_length=255, blank=False)
    weight = models.CharField(max_length=255, blank=True)
    reps = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.exercise
