# Generated by Django 5.0.2 on 2024-03-05 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tontine', '0002_utilisateur_nom_utilisateur_prenom_participation_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='participation',
            unique_together=set(),
        ),
    ]
