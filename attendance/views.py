class AttendanceViewSet(ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == "TEACHER":
            return Attendance.objects.filter(lesson__teacher=user)

        return Attendance.objects.all()

    def perform_create(self, serializer):
        lesson = serializer.validated_data["lesson"]
        user = self.request.user

        if user.role == "TEACHER" and lesson.teacher != user:
            raise PermissionDenied()

        serializer.save()