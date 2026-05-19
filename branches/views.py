from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Branch
from .serializers import BranchSerializer


class BranchViewSet(ModelViewSet):

    queryset = Branch.objects.all()

    serializer_class = BranchSerializer

    permission_classes = [IsAuthenticated]