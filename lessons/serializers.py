from rest_framework import serializers
from django.db.models import Q
from .models import Lesson


def check_conflicts(teacher, students, start, end):
    lessons = Lesson.objects.filter(status="SCHEDULED").filter(
        Q(teacher=teacher) |
        Q(student__in=students) |
        Q(group__students__in=students)
    ).distinct()

    for lesson in lessons:
        if start < lesson.end_time and lesson.start_time < end:
            return True
    return False


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"

    def validate(self, data):
        teacher = data.get("teacher")
        student = data.get("student")
        group = data.get("group")
        start = data.get("start_time")
        end = data.get("end_time")

        if not student and not group:
            raise serializers.ValidationError("Student or group required")

        if student and group:
            raise serializers.ValidationError("Only one of student or group allowed")

        if start >= end:
            raise serializers.ValidationError("Invalid time")

        students = []
        if student:
            students = [student]
        if group:
            students = list(group.students.all())

        if check_conflicts(teacher, students, start, end):
            raise serializers.ValidationError("Conflict detected")

        return data