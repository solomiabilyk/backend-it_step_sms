<<<<<<< Updated upstream
from django.shortcuts import render
from .models import Student


def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/students.html', {'students': students})
=======
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def get_queryset(self):
        user = self.request.user

        if user.role == "TEACHER":
            return Student.objects.none()

        return Student.objects.all()
>>>>>>> Stashed changes
