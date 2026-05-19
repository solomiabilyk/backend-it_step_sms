from django.test import TestCase
from django.utils import timezone
from datetime import timedelta

from users.models import User
from students.models import Student
from lessons.models import Lesson
from branches.models import Branch



class LessonConflictTest(TestCase):

    def setUp(self):

        self.branch = Branch.objects.create(
            name="Lviv Branch",
        )

        self.teacher = User.objects.create_user(
            phone="+380111111111",
            password="test123"
        )

        self.student = Student.objects.create(
            first_name="Ivan",
            last_name="Petrenko",
            phone="+380222222222",
            branch=self.branch
        )

    def test_teacher_conflict(self):

        start1 = timezone.now()
        end1 = start1 + timedelta(hours=1)

        Lesson.objects.create(
            teacher=self.teacher,
            student=self.student,
            start_time=start1,
            end_time=end1,
        )

        start2 = start1 + timedelta(minutes=30)
        end2 = start2 + timedelta(hours=1)

        conflict = (
            Lesson.objects.filter(
                teacher=self.teacher,
                start_time__lt=end2,
                end_time__gt=start2,
            ).exists()
        )

        self.assertTrue(conflict)