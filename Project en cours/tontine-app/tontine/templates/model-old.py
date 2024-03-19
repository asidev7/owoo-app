import random
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Group, Permission

from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(**extra_fields, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Utilisateur(AbstractUser):
    user_groups = models.ManyToManyField(Group, related_name='utilisateur_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='utilisateur_permissions', blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username

class CustomGroup(models.Model):
    GROUP_ROLE_CHOICES = [
        ('admin', 'Administrateur'),
        ('gestionnaire', 'Gestionnaire'),
        ('utilisateur', 'Utilisateur'),
    ]

    name = models.CharField(max_length=50, choices=GROUP_ROLE_CHOICES, unique=True)
    members = models.ManyToManyField(Utilisateur, related_name='custom_groups', blank=True)
    effectifs = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.get_name_display()} Group"



class Tontine(models.Model):
    DUREE_CHOICES = [
        (1, 'Journalière'),
        (7, 'Hebdomadaire'),
        (15, 'Quinzaine'),
        (30, 'Mensuelle'),
        (90, 'Trimestrielle'),
        (365, 'Annuelle'),
    ]
    membres = models.ManyToManyField(Utilisateur, related_name='tontines_membres')
    gestionnaire = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='tontines_gestionnaire')
    nom_tontine = models.CharField(max_length=255)
    description = models.TextField()
    montant_max = models.PositiveBigIntegerField()
    effectifs = models.PositiveBigIntegerField()
    date_debut = models.DateField()
    duree_tontine = models.PositiveIntegerField(choices=DUREE_CHOICES, default=30)
    code_access = models.PositiveBigIntegerField(unique=True,default=0)
    def generate_access_code(self):
        return random.randint(100000, 999999)  # Generate a random 6-digit number

    def save(self, *args, **kwargs):
        if not self.code_access:
            # Generate the access code only if it hasn't been set yet
            self.code_access = self.generate_access_code()
        super().save(*args, **kwargs)

    def ajouter_membre(self, user_profile, access_code=None):
        if self.membres.count() < self.effectifs:
            if access_code is None:
                access_code = self.generate_access_code()
            self.membres.add(user_profile)
            self.code_access = access_code
            self.save()
            try:
                Wallet.objects.create(membre=user_profile)
            except Exception as e:
                print(f"Error creating Wallet: {e}")
        else:
            raise ValueError("La tontine a atteint son effectif maximum")

    def supprimer_membre(self, user_profile):
        self.membres.remove(user_profile)
        # Supprimer également le portefeuille du membre
        Wallet.objects.filter(membre=user_profile).delete()

    def afficher_membres(self):
        print(f"Membres de la Tontine {self.nom_tontine}:")
        for membre in self.membres.all():
            print(f"User ID: {membre.user.id}, Username: {membre.user.username}")

    @classmethod
    def creer_tontine(cls, gestionnaire, nom_tontine, description, montant_max, effectifs, date_debut, duree_tontine):
        # Vérifier si le gestionnaire existe et s'il n'a pas déjà une tontine en cours
        gestionnaire = Utilisateur.objects.get(id=gestionnaire.id)
        tontine, created = cls.objects.get_or_create(gestionnaire=gestionnaire, defaults={
            'nom_tontine': nom_tontine,
            'description': description,
            'montant_max': montant_max,
            'effectifs': effectifs,
            'date_debut': date_debut,
            'duree_tontine': duree_tontine
        })

        if not created:
            raise ValueError("Le gestionnaire a déjà une tontine en cours.")

        return tontine

class Depot(models.Model):
    tontine = models.ForeignKey(Tontine, on_delete=models.CASCADE)
    membre = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_depot = models.DateField(auto_now_add=True)
    mode_paiement = models.CharField(max_length=50, null=True, blank=True)
    reference = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Depot de {self.montant} effectué par {self.membre.user.username} le {self.date_depot}"

class Retrait(models.Model):
    tontine = models.ForeignKey(Tontine, on_delete=models.CASCADE)
    membre = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_retrait = models.DateField(auto_now_add=True)
    mode_paiement = models.CharField(max_length=50, null=True, blank=True)
    reference = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"Retrait de {self.montant} effectué par {self.organisateur.username} pour {self.membre.user.username} le {self.date_retrait}"

class Wallet(models.Model):
    membre = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)
    solde = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Portefeuille de {self.membre.username} - Solde: {self.solde}"
