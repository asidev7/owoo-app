# Generated by Django 5.0.2 on 2024-03-13 11:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tontine', '0005_informationentreprise_logo_white'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('date_naissance', models.DateField(blank=True)),
                ('ville', models.CharField(max_length=255)),
                ('quatrier', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='depot',
            name='membre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tontine.membre'),
        ),
        migrations.AlterField(
            model_name='participation',
            name='membre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tontine.membre'),
        ),
        migrations.AlterField(
            model_name='retrait',
            name='membre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tontine.membre'),
        ),
        migrations.AlterField(
            model_name='tontine',
            name='membres',
            field=models.ManyToManyField(related_name='tontines_participees', through='tontine.Participation', to='tontine.membre'),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='membre',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tontine.membre'),
        ),
    ]
