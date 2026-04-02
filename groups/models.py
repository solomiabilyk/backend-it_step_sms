from django.db import models
from django.core.exceptions import ValidationError
from management.models import Branch, Student

class Group(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва групи")
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, verbose_name="Філія")
    students = models.ManyToManyField(Student, related_name='student_groups', verbose_name="Студенти", blank=True)
    status = models.CharField(max_length=10, default='ACTIVE', verbose_name="Статус")

    def __str__(self):
        return f"{self.name} ({self.branch.name})"

    def clean(self):
        """
        Перевірка: чи всі вибрані студенти належать до тієї ж філії, що й група.
        """
        
        if self.pk: 
            for student in self.students.all():
                if student.branch != self.branch:
                    raise ValidationError(
                        f"Помилка! Студент {student.first_name} з філії {student.branch.name} "
                        f"не може бути в групі філії {self.branch.name}."
                    )