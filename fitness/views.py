from django.shortcuts import render, redirect, get_object_or_404
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

        exercises = form.cleaned_data['exercise_name']
        form = ExerciseForm()
        return redirect('all_exercises')

    args = {'form': form, 'exercises': exercises}
    return render(request, 'fitness/exercises.html', args)
