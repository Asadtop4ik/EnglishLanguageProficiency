from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import getExams, IELTSViewSet, DuolingoViewSet, TOEFLViewSet, CEFRViewSet

router = DefaultRouter()
router.register(r'IELTS/ielts', IELTSViewSet, basename="ielts")
router.register(r'Duolingo/duolingo', DuolingoViewSet, basename="duolingo")
router.register(r'TOEFL/toefl', TOEFLViewSet, basename="toefl")
router.register(r'CEFR/cefr', CEFRViewSet, basename="cefr")


urlpatterns = [
    path('', include(router.urls)),
    path('getExams/', getExams, name="getExams"),
]
