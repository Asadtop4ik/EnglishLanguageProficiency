# Generated by Django 5.0.6 on 2024-06-10 18:56

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CEFR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listening', models.CharField(max_length=10)),
                ('reading', models.CharField(max_length=10)),
                ('writing', models.CharField(max_length=10)),
                ('speaking', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Duolingo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('literacy', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(160)])),
                ('conversation', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(160)])),
                ('comprehension', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(160)])),
                ('production', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(160)])),
            ],
        ),
        migrations.CreateModel(
            name='IELTS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listening', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9)])),
                ('reading', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9)])),
                ('writing', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9)])),
                ('speaking', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9)])),
            ],
        ),
        migrations.CreateModel(
            name='TOEFL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reading', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(30)])),
                ('listening', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(30)])),
                ('speaking', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(30)])),
                ('writing', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(30)])),
            ],
        ),
        migrations.CreateModel(
            name='Exams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cefr', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='english_tests.cefr')),
                ('duolingo', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='english_tests.duolingo')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ielts', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='english_tests.ielts')),
                ('toefl', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='english_tests.toefl')),
            ],
        ),
    ]
