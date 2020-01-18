from django.shortcuts import render, redirect
from .models import Task, Profile
from .forms import TaskForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from .decorators import unauthenticated_user, allowed_users


# Create your views here.
@login_required(login_url='login')
def index(request):
    tasks = Task.objects.filter(user_profile__user=request.user)
    form = TaskForm()

    context = {'tasks': tasks, 'form': form}
    return render(request, 'todo/index.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['create_task'])
def create_task(request):
    profile = Profile.objects.get(user=request.user)
    form = TaskForm(request.POST)
    if form.is_valid():
        task = form.save(commit=False)
        task.user_profile = profile
        task.save()
    return redirect('index')


@login_required(login_url='login')
@allowed_users(allowed_roles=['update_task'])
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


@login_required(login_url='login')
@allowed_users(allowed_roles=['delete_task'])
def delete_task(request, task_id):
    item = Task.objects.get(id=task_id)

    if request.method == 'POST':
        item.delete()
        return redirect('index')
    context = {
        'item': item
    }
    return render(request, 'todo/delete_task.html', context)


# signal is creating profile
@unauthenticated_user
def register_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, "Account was created for " + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'todo/register.html', context)


@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username or password is incorrect!')
    context = {}
    return render(request, 'todo/login.html', context)


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')
