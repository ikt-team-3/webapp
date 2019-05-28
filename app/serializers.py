from rest_framework import serializers
from .models import Predmet, Tema, Poraka


class TemaSerializer(serializers.ModelSerializer):
    post_count = serializers.SerializerMethodField()

    class Meta:
        model = Tema
        fields = ('id', 'post_count', 'naslov', 'avtor')

    def get_post_count(self, obj):
        return obj.poraka_set.count()


class PredmetSerializer(serializers.ModelSerializer):
    tema_count = serializers.SerializerMethodField()

    class Meta:
        model = Predmet
        fields = ('id', 'naslov', 'tema_count')

    def get_tema_count(self, obj):
        return obj.tema_set.count()


class PorakaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poraka
        fields = ('id', 'tekst', 'avtor')


class SinglePredmetSerializer(serializers.ModelSerializer):
    tema_set = TemaSerializer(many=True, read_only=True)

    class Meta:
        model = Predmet
        fields = '__all__'


class SingleTemaSerializer(serializers.ModelSerializer):
    poraka_set = PorakaSerializer(many=True, read_only=True)
    predmet = serializers.SerializerMethodField()

    class Meta:
        model = Tema
        fields = ('id', 'naslov', 'avtor', 'predmet', 'poraka_set')

    def get_predmet(self, obj):
        return obj.predmet.naslov
