from django.db import models


# Create your models here.
class HotSpot(models.Model):
    place = models.CharField(max_length=255, blank=False)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.place