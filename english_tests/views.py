from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Exams, IELTS, Duolingo, TOEFL, CEFR
from .serializers import ExamsSerializer, IELTS_Serializer, DuolingoSerializer, TOEFLSerializer, CEFRSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


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


@api_view(['GET'])
def getExams(request):
    if request.method == 'GET':
        exams = Exams.objects.all()
        serializer = ExamsSerializer(exams, many=True)
        return Response(serializer.data)

