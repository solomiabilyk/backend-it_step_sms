from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import (
    SubscriptionPlan,
    StudentSubscription
)

from .serializers import (
    SubscriptionPlanSerializer,
    StudentSubscriptionSerializer
)


class SubscriptionPlanViewSet(ModelViewSet):

    queryset = SubscriptionPlan.objects.all()

    serializer_class = SubscriptionPlanSerializer

    permission_classes = [IsAuthenticated]


class StudentSubscriptionViewSet(ModelViewSet):

    queryset = StudentSubscription.objects.all()

    serializer_class = StudentSubscriptionSerializer

    permission_classes = [IsAuthenticated]