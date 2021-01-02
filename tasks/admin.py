from django.contrib import admin
from .models import Task, ColourTheme

# Register your models here.
admin.site.register(Task)
admin.site.register(ColourTheme)
