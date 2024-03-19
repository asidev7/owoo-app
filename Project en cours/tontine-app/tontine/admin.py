from django.contrib import admin

from tontine.models import Participation, Tontine,Utilisateur,InformationEntreprise, Membre

# Register your models here.
admin.site.register(Tontine)
admin.site.register(Utilisateur)
admin.site.register(Participation)
admin.site.register(InformationEntreprise)
admin.site.register(Membre)