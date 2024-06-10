from django.test import TestCase
from .models import IELTS, Duolingo, TOEFL, CEFR, Exams
from custom_auth.models import User


class ModelsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password', gender='Male')
        self.ielts = IELTS.objects.create(listening=8.5, reading=7.5, writing=6.5, speaking=7.0)
        self.duolingo = Duolingo.objects.create(literacy=120, conversation=130, comprehension=140, production=150)
        self.toefl = TOEFL.objects.create(reading=25, listening=27, speaking=23, writing=24)
        self.cefr = CEFR.objects.create(listening='C1', reading='B2', writing='C2', speaking='B1')
        self.exam = Exams.objects.create(ielts=self.ielts, duolingo=self.duolingo, toefl=self.toefl, cefr=self.cefr, user=self.user)

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertEqual(self.user.gender, 'Male')

    def test_ielts_creation(self):
        self.assertEqual(self.ielts.listening, 8.5)
        self.assertEqual(self.ielts.reading, 7.5)
        self.assertEqual(self.ielts.writing, 6.5)
        self.assertEqual(self.ielts.speaking, 7.0)

    def test_duolingo_creation(self):
        self.assertEqual(self.duolingo.literacy, 120)
        self.assertEqual(self.duolingo.conversation, 130)
        self.assertEqual(self.duolingo.comprehension, 140)
        self.assertEqual(self.duolingo.production, 150)

    def test_toefl_creation(self):
        self.assertEqual(self.toefl.reading, 25)
        self.assertEqual(self.toefl.listening, 27)
        self.assertEqual(self.toefl.speaking, 23)
        self.assertEqual(self.toefl.writing, 24)

    def test_cefr_creation(self):
        self.assertEqual(self.cefr.listening, 'C1')
        self.assertEqual(self.cefr.reading, 'B2')
        self.assertEqual(self.cefr.writing, 'C2')
        self.assertEqual(self.cefr.speaking, 'B1')

    def test_exam_creation(self):
        self.assertEqual(self.exam.ielts, self.ielts)
        self.assertEqual(self.exam.duolingo, self.duolingo)
        self.assertEqual(self.exam.toefl, self.toefl)
        self.assertEqual(self.exam.cefr, self.cefr)
        self.assertEqual(self.exam.user, self.user)
