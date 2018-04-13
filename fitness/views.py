from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DeleteView
from django.views.decorators.http import require_POST
from .models import Exercise
from .forms import ExerciseForm


# Create your views here.
def all_exercises(request):
    # print(Exercise.objects.all())
    exercises = Exercise.objects.all()

    form = ExerciseForm(request.POST)

    # This section of code is what creates the form in the template.
    if form.is_valid():
        exercise_name = form.save(commit=False)
        exercise_name.user = request.user
        exercise_name.save()

        exercises = form.cleaned_data['exercise']
        form = ExerciseForm()
        return redirect('all_exercises')

    args = {'form': form, 'exercises': exercises}
    return render(request, 'fitness/exercises.html', args)


# Function associated to the delete button
def delete_exercise(request, id):
    exercise = Exercise.objects.get(id=id)
    if request.method == 'POST':
        exercise.delete()
        return redirect('all_exercises')

    args = {'exercise': exercise}
    return render(request, 'fitness/delete.html', args)
