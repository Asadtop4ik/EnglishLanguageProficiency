from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class IELTS(models.Model):
    listening = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(9)])
    reading = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(9)])
    writing = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(9)])
    speaking = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(9)])

class Duolingo(models.Model):
    literacy = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(160)])
    conversation = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(160)])
    comprehension = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(160)])
    production = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(160)])

class TOEFL(models.Model):
    reading = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)])
    listening = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)])
    speaking = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)])
    writing = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(30)])

class CEFR(models.Model):
    listening = models.CharField(max_length=10)
    reading = models.CharField(max_length=10)
    writing = models.CharField(max_length=10)
    speaking = models.CharField(max_length=10)

class Exams(models.Model):
    ielts = models.OneToOneField(IELTS, on_delete=models.CASCADE, null=True, blank=True)
    duolingo = models.OneToOneField(Duolingo, on_delete=models.CASCADE, null=True, blank=True)
    toefl = models.OneToOneField(TOEFL, on_delete=models.CASCADE, null=True, blank=True)
    cefr = models.OneToOneField(CEFR, on_delete=models.CASCADE, null=True, blank=True)
    user = models.OneToOneField('custom_auth.User', on_delete=models.CASCADE)
