from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

from .models import Task
from .forms import TaskForm


# Create your views here.
def all_tasks(request):
    tasks = Task.objects.all()

    form = TaskForm(request.POST)

    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.save()

    args = {'form': form, 'tasks': tasks}
    return render(request, 'todo.html', args)