from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Exams
from .serializers import ExamsSerializer


class ExamsViewSet(viewsets.ModelViewSet):
    queryset = Exams.objects.all()
    serializer_class = ExamsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Exams.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
