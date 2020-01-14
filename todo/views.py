from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


# Create your views here.

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')

    context = {'tasks': tasks, 'form': form}
    return render(request, 'todo/index.html', context)


def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('index')

    context = {'form': form}
    return render(request, 'todo/update_task.html', context)


def delete_task(request, task_id):
    item = Task.objects.get(id=task_id)

    if request.method == 'POST':
        item.delete()
        return redirect('index')
    context = {
        'item': item
    }
    return render(request, 'todo/delete_task.html', context)
