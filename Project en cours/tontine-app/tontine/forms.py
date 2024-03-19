from django import forms
from django.contrib.auth.forms import AuthenticationForm

from tontine.models import Membre, Participation, Tontine

class CustomLoginForm(AuthenticationForm):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-input'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'] = self.fields.pop('username')  # Remove the default username field


class TontineForm(forms.ModelForm):
    class Meta:
        model = Tontine
        fields = '__all__'
        exclude =['gestionnaire','membres']
        widgets = {
            'nom_tontine': forms.TextInput(attrs={'class': 'form-input w-100'}),
            'description': forms.Textarea(attrs={'class': 'form-input w-100'}),
            'montant_max': forms.NumberInput(attrs={'class': 'form-input w-100'}),
            'effectifs_max': forms.NumberInput(attrs={'class': 'form-input w-100'}),
            'duree_paiement': forms.Select(attrs={'class': 'form-input w-100'}),
            'code_access': forms.NumberInput(attrs={'class': 'form-input w-100'}),
            'date_debut': forms.DateInput(attrs={'class': 'form-input w-100'}),
            'membres': forms.SelectMultiple(attrs={'class': 'form-input w-100'}),
        }



class MembreForm(forms.ModelForm):
    class Meta:
        model = Membre
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-input w-100'}),
            'prenom': forms.TextInput(attrs={'class': 'form-input w-100'}),
            'date_naissance': forms.DateInput(attrs={'class': 'form-input w-100', 'type': 'date'}),
            'ville': forms.TextInput(attrs={'class': 'form-input w-100'}),
            'quatrier': forms.TextInput(attrs={'class': 'form-input w-100'}),
        }
        

class ParticipationForm(forms.ModelForm):
    class Meta:
        model = Participation
        fields = '__all__'
        widgets = {
            'membre': forms.Select(attrs={'class': 'form-control'}),
            'tontine': forms.Select(attrs={'class': 'form-control'}),
            'montant_journalier': forms.NumberInput(attrs={'class': 'form-control'}),
            'date_adhesion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }