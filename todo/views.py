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
        tasks = form.save(commit=False)
        tasks.user = request.user
        tasks.save()

        tasks = form.cleaned_data['post']
        form = TaskForm()
        return redirect('todo.html')

    args = {'form': form, 'tasks': tasks}
    return render(request, 'todo.html', args)