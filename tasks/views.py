from django.shortcuts import render

# Create your views here.


def get_tasks(request):
    """ view for main tasks list """
    return render(request, 'tasks/tasks.html')
