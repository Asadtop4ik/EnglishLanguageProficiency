from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Exams, IELTS, Duolingo, TOEFL, CEFR
from .serializers import ExamsSerializer, IELTS_Serializer, DuolingoSerializer, TOEFLSerializer, CEFRSerializer


class ExamsViewSet(viewsets.ModelViewSet):
    queryset = Exams.objects.all()
    serializer_class = ExamsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Exams.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class IELTSViewSet(viewsets.ModelViewSet):
    queryset = IELTS.objects.all()
    serializer_class = IELTS_Serializer
    permission_classes = [IsAuthenticated]


class DuolingoViewSet(viewsets.ModelViewSet):
    queryset = Duolingo.objects.all()
    serializer_class = DuolingoSerializer
    permission_classes = [IsAuthenticated]


class TOEFLViewSet(viewsets.ModelViewSet):
    queryset = TOEFL.objects.all()
    serializer_class = TOEFLSerializer
    permission_classes = [IsAuthenticated]


class CEFRViewSet(viewsets.ModelViewSet):
    queryset = CEFR.objects.all()
    serializer_class = CEFRSerializer
    permission_classes = [IsAuthenticated]
