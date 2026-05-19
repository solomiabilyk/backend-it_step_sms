from django.test import TestCase

from users.models import User
from students.models import Student
from lessons.models import Lesson
from attendance.models import Attendance
from branches.models import Branch


from django.utils import timezone
from datetime import timedelta


class AttendanceTest(TestCase):

    def setUp(self):

        self.branch = Branch.objects.create(
            name="Lviv Branch",
        )

        self.teacher = User.objects.create_user(
            phone="+380123456789",
            password="test123"
        )

        self.student = Student.objects.create(
            first_name="Anna",
            last_name="Ivanova",
            phone="+380987654321",
            branch=self.branch
        )

        self.lesson = Lesson.objects.create(
            teacher=self.teacher,
            student=self.student,
            start_time=timezone.now(),
            end_time=timezone.now() + timedelta(hours=1),
        )

    def test_mark_attendance(self):

        attendance = Attendance.objects.create(
            lesson=self.lesson,
            student=self.student,
            status="PRESENT"
        )

        self.assertEqual(attendance.status, "PRESENT")