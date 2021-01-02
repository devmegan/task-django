from django.db import models

# Create your models here.


class Task(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    urgent = models.BooleanField(blank=False, default=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name


class ColourTheme(models.Model):
    colour = models.CharField(max_length=20, null=False, default="yellow")

    def __str__(self):
        return self.colour
