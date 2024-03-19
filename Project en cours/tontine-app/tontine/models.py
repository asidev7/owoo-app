from django.db import models
from django.db.models import Count
from django.db.models.functions import Coalesce
# Create your models here.

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)



class Utilisateur(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Membre(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    date_naissance = models.DateField(blank=True)
    ville = models.CharField(max_length=255)
    quatrier = models.CharField(max_length=255)


class Participation(models.Model):
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    tontine = models.ForeignKey('Tontine', on_delete=models.CASCADE)
    montant_journalier = models.DecimalField(max_digits=10, decimal_places=2)
    date_adhesion = models.DateField(auto_now_add=True)



class Tontine(models.Model):
    DUREE_CHOICES = [
        (1, 'Journalière'),
        (7, 'Hebdomadaire'),
        (30, 'Mensuelle'),
    ]
    gestionnaire = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='tontines_gerees')
    nom_tontine = models.CharField(max_length=255)
    description = models.TextField()
    montant_max = models.PositiveBigIntegerField()
    effectifs_max = models.PositiveIntegerField()
    duree_paiement = models.PositiveIntegerField(choices=DUREE_CHOICES)
    date_debut = models.DateField(auto_now_add=True)
    membres = models.ManyToManyField(Membre, through=Participation,blank=True, related_name='tontines_participees')

    def save(self, *args, **kwargs):
        # Vous pouvez ajuster le montant_max en fonction de la durée
        if self.duree_paiement == 1:  # Journalière
            self.montant_max = self.montant_max * 30  # Supposons 30 jours par mois
        super().save(*args, **kwargs)
    @property
    def participant_count(self):
        return self.membres.annotate(dummy=Coalesce(Count('participation'), 0)).count()
    
    def __str__(self) -> str:
        return self.nom_tontine


class Paiement(models.Model):
    participation = models.ForeignKey(Participation, on_delete=models.CASCADE)
    montant_paiement = models.DecimalField(max_digits=10, decimal_places=2)
    date_paiement = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.date_paiement

class Depot(models.Model):
    tontine = models.ForeignKey(Tontine, on_delete=models.CASCADE)
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_depot = models.DateField(auto_now_add=True)

class Retrait(models.Model):
    tontine = models.ForeignKey(Tontine, on_delete=models.CASCADE)
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_retrait = models.DateField(auto_now_add=True)

class Wallet(models.Model):
    membre = models.OneToOneField(Membre, on_delete=models.CASCADE)
    solde = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class InformationEntreprise(models.Model):
    nom_entreprise = models.CharField(max_length=40)
    logo = models.ImageField(upload_to="logo")
    logo_white = models.ImageField(upload_to="logo")
    description = models.TextField()
