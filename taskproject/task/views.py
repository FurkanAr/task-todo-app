from django.shortcuts import redirect, render
from .models import Task
from .forms import TaskForm
from django.contrib import messages

def getTask(request):
    tasks = Task.objects.all().order_by('date')
    context = {
        'tasks' : tasks
    }
    return render(request, 'task/task.html', context)

def getTaskForm(request):
    if request.method == "POST":    
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            task_name = form.cleaned_data.get('title')
            messages.debug(request, f'{task_name} was added successfully!!')
            return redirect('/task/list')
    
    form = TaskForm()
    context = {
        'form' : form,
    } 
    return render(request, 'task/taskform.html', context)

def updateTaskForm(request, id):
    task = Task.objects.get(id = id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
            task_name = form.cleaned_data.get('title')
            messages.success(request, f'Task: {task_name} updated!!')
            return redirect('/task/list')
    else:
        form = TaskForm(instance=task)

    context = {
        'form': form,
    }
    return render(request, 'task/updateform.html', context)

def deleteTask(request, id):
    task = Task.objects.get(id = id)
    task.delete()
    messages.error(request, f'Task: {task.title} deleted!!')
    return redirect('/task/list')