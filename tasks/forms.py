from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    # form to add a new task
    class Meta:
        model = Task
        fields = ['name', 'urgent', 'done']
