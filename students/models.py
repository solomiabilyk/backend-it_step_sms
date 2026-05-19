from django.db import models
from branches.models import Branch


class Student(models.Model):

    STATUS_CHOICES = [
        ("ACTIVE", "Active"),
        ("ARCHIVED", "Archived"),
    ]

    first_name = models.CharField(max_length=255)

    last_name = models.CharField(max_length=255)

    phone = models.CharField(max_length=20)

    branch = models.ForeignKey(
        Branch,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ACTIVE"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Group(models.Model):

    STATUS_CHOICES = [
        ("ACTIVE", "Active"),
        ("ARCHIVED", "Archived"),
    ]

    name = models.CharField(max_length=255)

    branch = models.ForeignKey(
        Branch,
        on_delete=models.CASCADE
    )

    students = models.ManyToManyField(Student)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ACTIVE"
    )

    def __str__(self):
        return self.name