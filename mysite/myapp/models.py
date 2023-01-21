from django.db import models

# Create your models here.

class Logger(models.Model):
    fist_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    time_log = models.TimeField(help_text="Enter the exact time!")

class Timer(models.Model):
    time_log = models.TimeField(help_text="Enter the exact time!")
    time_in = models.TimeField(help_text="Enter the exact time!")
    time_out = models.TimeField(help_text="Enter the exact time!")
