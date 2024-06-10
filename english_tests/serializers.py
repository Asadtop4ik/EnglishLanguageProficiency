from rest_framework import serializers
from .models import IELTS, Duolingo, TOEFL, CEFR, Exams

class IELTS_Serializer(serializers.ModelSerializer):
    class Meta:
        model = IELTS
        fields = '__all__'

class DuolingoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Duolingo
        fields = '__all__'

class TOEFLSerializer(serializers.ModelSerializer):
    class Meta:
        model = TOEFL
        fields = '__all__'

class CEFRSerializer(serializers.ModelSerializer):
    class Meta:
        model = CEFR
        fields = '__all__'

class ExamsSerializer(serializers.ModelSerializer):
    ielts = IELTS_Serializer()
    duolingo = DuolingoSerializer()
    toefl = TOEFLSerializer()
    cefr = CEFRSerializer()

    class Meta:
        model = Exams
        fields = ['id', 'user', 'ielts', 'duolingo', 'toefl', 'cefr']

    def create(self, validated_data):
        ielts_data = validated_data.pop('ielts', None)
        duolingo_data = validated_data.pop('duolingo', None)
        toefl_data = validated_data.pop('toefl', None)
        cefr_data = validated_data.pop('cefr', None)

        ielts = IELTS.objects.create(**ielts_data) if ielts_data else None
        duolingo = Duolingo.objects.create(**duolingo_data) if duolingo_data else None
        toefl = TOEFL.objects.create(**toefl_data) if toefl_data else None
        cefr = CEFR.objects.create(**cefr_data) if cefr_data else None

        exam = Exams.objects.create(
            user=validated_data['user'],
            ielts=ielts,
            duolingo=duolingo,
            toefl=toefl,
            cefr=cefr
        )

        return exam

    def update(self, instance, validated_data):
        if 'ielts' in validated_data:
            IELTS.objects.filter(id=instance.ielts.id).update(**validated_data.pop('ielts'))
        if 'duolingo' in validated_data:
            Duolingo.objects.filter(id=instance.duolingo.id).update(**validated_data.pop('duolingo'))
        if 'toefl' in validated_data:
            TOEFL.objects.filter(id=instance.toefl.id).update(**validated_data.pop('toefl'))
        if 'cefr' in validated_data:
            CEFR.objects.filter(id=instance.cefr.id).update(**validated_data.pop('cefr'))

        instance.save()
        return instance
