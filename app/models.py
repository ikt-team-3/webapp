from django.db import models
from django.contrib.auth.models import User


class Korisnik(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ime = models.CharField(max_length=100)
    prezime = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "korisnici"


class Predmet(models.Model):
    naslov = models.CharField(max_length=200)
    naslov_id = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "predmeti"

    def __str__(self):
        return self.naslov


class Tema(models.Model):
    naslov = models.CharField(max_length=200)
    avtor = models.ForeignKey(Korisnik, related_name='temi', on_delete=models.SET_NULL, blank=True, null=True)
    predmet = models.ForeignKey(Predmet, related_name='temi', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "temi"

    def __str__(self):
        return self.naslov


class Poraka(models.Model):
    tekst = models.TextField()
    avtor = models.ForeignKey(Korisnik, related_name='poraki', on_delete=models.SET_NULL, blank=True, null=True)
    tema = models.ForeignKey(Tema, related_name='poraki', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "poraki"

    def __str__(self):
        return self.tekst
