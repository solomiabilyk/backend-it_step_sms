from django.db import models
from users.models import User
from students.models import Student, Group


class Lesson(models.Model):
    STATUS_CHOICES = [
        ("SCHEDULED", "Scheduled"),
        ("COMPLETED", "Completed"),
        ("CANCELLED", "Cancelled"),
    ]

    teacher = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    student = models.ForeignKey(
        Student,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    group = models.ForeignKey(
        Group,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    start_time = models.DateTimeField()

    end_time = models.DateTimeField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="SCHEDULED"
    )

    def get_students(self):
        if self.student:
            return [self.student]

        if self.group:
            return list(self.group.students.all())

        return []

    def __str__(self):
        return f"{self.teacher} | {self.start_time}"