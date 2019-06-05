from django.contrib import admin
from .models import Predmet, Tema, Poraka, Korisnik, Profesor, Prostorija, Termin, UserTermin
# Register your models here.


class PredmetAdmin(admin.ModelAdmin):
    list_display = ('naslov', 'naslov_id')


class TemaAdmin(admin.ModelAdmin):
    list_display = ('naslov', 'predmet', 'avtor')


class PorakaAdmin(admin.ModelAdmin):
    list_display = ('tekst', 'avtor', 'tema', 'timestamp')


class UserTerminInline(admin.StackedInline):
    model = UserTermin
    extra = 1


class KorisnikAdmin(admin.ModelAdmin):
    inlines = [UserTerminInline]


class TerminAdmin(admin.ModelAdmin):
    list_display = ('id', 'predmet', 'profesor', 'prostorija', 'vreme', 'den', 'casovi')


admin.site.register(Predmet, PredmetAdmin)
admin.site.register(Tema, TemaAdmin)
admin.site.register(Poraka, PorakaAdmin)
admin.site.register(Korisnik, KorisnikAdmin)
admin.site.register(Profesor)
admin.site.register(Prostorija)
admin.site.register(Termin, TerminAdmin)
