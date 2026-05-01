<<<<<<< Updated upstream
from django.shortcuts import render

# Create your views here.
=======
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Lesson
from .serializers import LessonSerializer
from rest_framework.exceptions import PermissionDenied

class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == "TEACHER":
            return Lesson.objects.filter(teacher=user)

        return Lesson.objects.all()

    def perform_create(self, serializer):
        if self.request.user.role != "ADMIN":
            raise PermissionDenied()

        serializer.save()

    def perform_update(self, serializer):
        if self.request.user.role != "ADMIN":
            raise PermissionDenied()

        serializer.save()

    def perform_destroy(self, instance):
        if self.request.user.role != "ADMIN":
            raise PermissionDenied()

        instance.delete()
>>>>>>> Stashed changes
