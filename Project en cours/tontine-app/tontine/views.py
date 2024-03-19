from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from tontine.forms import CustomLoginForm, MembreForm, ParticipationForm, TontineForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model  # Use get_user_model to get the User model
from django.db.models import Count
from django.db.models import Sum
from tontine.models import Depot, Membre, Participation, Retrait, Tontine
from django.contrib.auth import logout

from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView

User = get_user_model()

# Create your views here.
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')  # Replace 'login' with the actual login URL pattern
def homepage(request):
    total_tontines = Tontine.objects.filter(gestionnaire=request.user).count()
    total_deposits = Depot.objects.aggregate(Sum('montant'))['montant__sum'] or 0
    total_withdrawals = Retrait.objects.aggregate(Sum('montant'))['montant__sum'] or 0
    total_participations = Participation.objects.count()
    params ={
        'total_tontines':total_tontines,
        'total_deposits':total_deposits,
        'total_withdrawals':total_withdrawals,
        'tototal_participations':total_participations
    }
    return render(request,
                  'main/home.html',params)

def connexion(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Assuming the input field name is 'email'
        password = request.POST.get('password')

        try:
            # Use your custom user model for querying based on email
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Utilisateur n'existe pas")
            return render(request, 'main/signin.html')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            # Log in the authenticated user
            login(request, user)
            return redirect(homepage)  # Replace 'homepage' with the actual URL name or path
        else:
            messages.error(request, 'Email or password is not correct')

    return render(request, 'main/signin.html')

def logout_view(request):
    logout(request)
    # Redirect to a specific URL after logout, or to the homepage
    return redirect(connexion)  # Replace 'home' with the name of your desired URL pattern


class TontineListView(ListView):
    model = Tontine
    template_name = 'main/liste_tontine.html'
    context_object_name = 'tontines'
    def get_queryset(self):
        return Tontine.objects.filter(gestionnaire=self.request.user)

class TontineUpdateView(UpdateView):
    model = Tontine
    template_name = 'main/modifier-tontine.html'
    fields = ['nom_tontine', 'description', 'montant_max', 'effectifs_max', 'duree_paiement']
    success_url = reverse_lazy('tontine_list')

class TontineDeleteView(DeleteView):
    model = Tontine
    template_name = 'main/tontine_confirm_delete.html'
    success_url = reverse_lazy('tontine_list')


def AjouterTontine(request):
    if request.method == 'POST':
        form = TontineForm(request.POST)
        if form.is_valid():
            tontine = form.save(commit=False)
            tontine.gestionnaire = request.user 
            form.save()
            return redirect(homepage)  # Redirect to some success URL
    else:
        form = TontineForm()
    params ={
        'form':form
    }
    return render(request,'main/ajouter-tontine.html',params)

def membreTontine(request,tontine_id):
    particpant = Participation.get_object_or_404(Participation, tontine=tontine_id)

    return render(request,'main/membretontine.html')



def AjouterMembre(request):
    if request.method == 'POST':
        form = MembreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/ajouter-participant')  # Redirect to some success URL
    else:
        form = MembreForm()
    params ={
        'form':form
    }
    return render(request,'main/ajouterMembre.html',params)


def AjouterParticipant(request,member_id):
    membre = get_object_or_404(Membre, pk=member_id)  # Retrieve the Membre instance using the member_id
    if request.method == 'POST':
        form = ParticipationForm(request.POST)
        if form.is_valid():
            participation = form.save(commit=False)
            participation.membre = membre  # Associate the Membre instance with the Participation
            participation.save()
            return redirect('/list-membre')  # Redirect to some success URL
    else:
        form = ParticipationForm()
    params ={
        'form':form
    }
    return render(request,'main/ajouterParticipant.html',params)



class MembreListView(ListView):
    model = Participation
    template_name = 'main/liste_membre.html'
    context_object_name = 'participants'
    def get_queryset(self):
        return Participation.objects.filter(tontine__gestionnaire=self.request.user)
