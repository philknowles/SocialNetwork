from django.contrib import admin

from .models import Exercise
from .forms import ExerciseForm


# Register your models here.
@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
        form = ExerciseForm
        list_display = ('exercise', 'weight', 'reps', 'sets', 'exercise_date', )
