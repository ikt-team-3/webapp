from rest_framework import serializers
from .models import Predmet, Tema, Poraka, Profesor, Termin


class TemaSerializer(serializers.ModelSerializer):
    post_count = serializers.SerializerMethodField()
    last_post_time = serializers.SerializerMethodField()

    class Meta:
        model = Tema
        fields = ('id', 'post_count', 'naslov', 'last_post_time')

    def get_post_count(self, obj):
        return obj.poraki.count()

    def get_last_post_time(self, obj):
        return obj.poraki.latest('timestamp').timestamp


class PredmetSerializer(serializers.ModelSerializer):
    tema_count = serializers.SerializerMethodField()

    class Meta:
        model = Predmet
        fields = ('id', 'naslov', 'tema_count')

    def get_tema_count(self, obj):
        return obj.temi.count()


class PorakaSerializer(serializers.ModelSerializer):
    avtor_ime = serializers.SerializerMethodField()

    class Meta:
        model = Poraka
        fields = ('id', 'tekst', 'avtor_ime', 'timestamp')

    def get_avtor_ime(self, obj):
        return obj.avtor.ime + " " + obj.avtor.prezime


class SinglePredmetSerializer(serializers.ModelSerializer):
    temi = TemaSerializer(many=True, read_only=True)

    class Meta:
        model = Predmet
        fields = '__all__'


class SingleTemaSerializer(serializers.ModelSerializer):
    poraki = PorakaSerializer(many=True, read_only=True)
    predmet = serializers.SerializerMethodField()
    avtor_ime = serializers.SerializerMethodField()

    class Meta:
        model = Tema
        fields = ('id', 'naslov', 'avtor_ime', 'predmet', 'poraki')

    def get_predmet(self, obj):
        return obj.predmet.naslov

    def get_avtor_ime(self, obj):
        return obj.avtor.ime + " " + obj.avtor.prezime


class ProfesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = '__all__'


class TerminSerializer(serializers.ModelSerializer):
    predmet = serializers.SerializerMethodField()
    profesor = serializers.SerializerMethodField()
    prostorija = serializers.SerializerMethodField()

    class Meta:
        model = Termin
        fields = '__all__'

    def get_predmet(self, obj):
        return obj.predmet.naslov

    def get_profesor(self, obj):
        return obj.profesor.prezime + ' ' + obj.profesor.titula + ' ' + obj.profesor.ime

    def get_prostorija(self, obj):
        return obj.prostorija.oznaka