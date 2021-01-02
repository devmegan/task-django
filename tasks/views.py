from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, ColourTheme
from .forms import TaskForm
# Create your views here.


def get_tasks(request):
    """ view for main tasks list """
    # task filtering
    filter = 'All'
    if request.GET:
        if 'complete' in request.GET:
            tasks = Task.objects.filter(done=True) or None
            filter = 'Complete'
        elif 'incomplete' in request.GET:
            tasks = Task.objects.filter(done=False) or None
            filter = 'Incomplete'
        elif 'urgent' in request.GET:
            tasks = Task.objects.filter(urgent=True) or None
            filter = 'Urgent'
        else:
            # something's gone wrong, just show all tasks
            tasks = Task.objects.all()
    else:
        tasks = Task.objects.all()
    colour = ColourTheme.objects.all()
    add_task_form = TaskForm()
    if request.method == 'POST':
        if 'taskId' in request.POST:
            add_task_form = TaskForm(request.POST)
            if add_task_form.is_valid():
                add_task_form.save()
            return redirect('tasks')
        elif 'colour' in request.POST:
            # handle users choice of colour theme
            colourObj = get_object_or_404(ColourTheme)
            colourObj.colour = request.POST['colour']
            colourObj.save()
            return redirect('tasks')

    context = {
        'tasks': tasks,
        'colour': colour[0],
        'filter': filter,
        'add_task_form': add_task_form,
    }
    return render(request, 'tasks/tasks.html', context)


def toggle_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.done = not task.done  # invert task status
    task.save()
    return redirect('tasks')


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('tasks')
