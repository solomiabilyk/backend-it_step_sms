from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = [
            "id",
            "first_name",
            "last_name",
            "phone",
            "email",
            "status",
            "branch",
        ]

    def validate_phone(self, value):
        if not value.startswith("+"):
            raise serializers.ValidationError("Phone must start with +")
        return value