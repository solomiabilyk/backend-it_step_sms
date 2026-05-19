from rest_framework import serializers

from .models import (
    SubscriptionPlan,
    StudentSubscription
)


class SubscriptionPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubscriptionPlan
        fields = "__all__"


class StudentSubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentSubscription
        fields = "__all__"