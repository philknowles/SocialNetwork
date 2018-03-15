from django.db import models


# Create your models here.
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=100)
    done = models.BooleanField(default=False)

    def __str__(self):
        if self.done:
            return "%s (done)" % self.task_name
        else:
            return self.task_name
