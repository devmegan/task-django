from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
# Create your views here.


def get_tasks(request):
    """ view for main tasks list """
    tasks = Task.objects.all()
    add_task_form = TaskForm()
    if request.method == 'POST':
        add_task_form = TaskForm(request.POST)
        if add_task_form.is_valid():
            add_task_form.save()
        return redirect('tasks')

    context = {
        'tasks': tasks,
        'add_task_form': add_task_form,
    }
    return render(request, 'tasks/tasks.html', context)
