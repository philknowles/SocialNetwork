from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

from .models import Task
from .forms import TaskForm


# Create your views here.
def all_tasks(request):
    tasks = Task.objects.all()

    form = TaskForm(request.POST)

    if form.is_valid():
        task_name = form.save(commit=False)
        task_name.user = request.user
        task_name.save()

        tasks = form.cleaned_data['task_name']
        form = TaskForm()
        return redirect('all_tasks')

    args = {'form': form, 'tasks': tasks}
    return render(request, 'todo.html', args)