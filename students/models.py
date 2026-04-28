from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Group(models.Model):
    name = models.CharField(max_length=255)
    students = models.ManyToManyField(Student)

    class Meta:
        verbose_name = "Study Group"
        verbose_name_plural = "Study Groups"

    def __str__(self):
        return self.name