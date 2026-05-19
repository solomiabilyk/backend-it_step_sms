from django.db import models

from branches.models import Branch
from subjects.models import Subject
from students.models import Student


class SubscriptionPlan(models.Model):

    PLAN_TYPES = [
        ("INDIVIDUAL", "Individual"),
        ("GROUP", "Group"),
    ]

    name = models.CharField(max_length=255)

    branch = models.ForeignKey(
        Branch,
        on_delete=models.CASCADE
    )

    subjects = models.ManyToManyField(Subject)

    plan_type = models.CharField(
        max_length=20,
        choices=PLAN_TYPES
    )

    lessons_per_month = models.IntegerField()

    price_per_lesson = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return self.name


class StudentSubscription(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE
    )

    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE
    )

    plan = models.ForeignKey(
        SubscriptionPlan,
        on_delete=models.CASCADE
    )

    start_date = models.DateField()

    def __str__(self):
        return f"{self.student} - {self.plan}"