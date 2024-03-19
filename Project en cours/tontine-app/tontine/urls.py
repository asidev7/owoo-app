from django.urls import path

from tontine.views import  AjouterMembre, AjouterParticipant, AjouterTontine, MembreListView, connexion, homepage, TontineListView, TontineUpdateView, TontineDeleteView, logout_view

urlpatterns = [
    path('',homepage),
    path('login',connexion,name="login"),
    path('tontines/', TontineListView.as_view(), name='tontine_list'),
    path('tontine/<int:pk>/edit/', TontineUpdateView.as_view(), name='tontine_edit'),
    path('tontine/<int:pk>/delete/', TontineDeleteView.as_view(), name='tontine_delete'),
    path('ajouter-tontine',AjouterTontine,name="tontine_add"),
    path('ajouter-membre',AjouterMembre,name="add_member"),
    path('liste-membre',MembreListView.as_view()),
    path('ajouter-participant',AjouterParticipant),
    path('logout',logout_view)

]
