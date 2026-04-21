
from django.db import models

class Lesson(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
