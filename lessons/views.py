from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from .models import Lesson
from .serializers import LessonSerializer


class LessonViewSet(ModelViewSet):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]
    queryset = Lesson.objects.all()

    def get_queryset(self):
        user = self.request.user

        # викладач бачить тільки свої уроки
        if hasattr(user, "role") and user.role == "TEACHER":
            return Lesson.objects.filter(teacher=user)

        return Lesson.objects.all()

    def perform_create(self, serializer):
        if getattr(self.request.user, "role", None) != "ADMIN":
            raise PermissionDenied("Only admin can create lessons")

        serializer.save()

    def perform_update(self, serializer):
        if getattr(self.request.user, "role", None) != "ADMIN":
            raise PermissionDenied("Only admin can update lessons")

        serializer.save()

    def perform_destroy(self, instance):
        if getattr(self.request.user, "role", None) != "ADMIN":
            raise PermissionDenied("Only admin can delete lessons")

        instance.delete()