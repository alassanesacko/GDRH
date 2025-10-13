from django.shortcuts import render, redirect, get_object_or_404
from .models import Stagiaire
from django.contrib.auth.decorators import login_required
from django import forms

class StagiaireForm(forms.ModelForm):
    class Meta:
        model = Stagiaire
        fields = ['nom', 'prenom', 'email', 'telephone', 'ecole', 'date_debut', 'date_fin', 'sujet']

@login_required
def liste_stagiaires(request):
    stagiaires = Stagiaire.objects.all()
    return render(request, 'stagiaires/liste_stagiaires.html', {'stagiaires': stagiaires})

@login_required
def ajouter_stagiaire(request):
    if request.method == 'POST':
        form = StagiaireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_stagiaires')
    else:
        form = StagiaireForm()
    return render(request, 'stagiaires/ajouter_stagiaire.html', {'form': form})

@login_required
def detail_stagiaire(request, pk):
    stagiaire = get_object_or_404(Stagiaire, pk=pk)
    return render(request, 'stagiaires/detail_stagiaire.html', {'stagiaire': stagiaire})

@login_required
def modifier_stagiaire(request, pk):
    stagiaire = get_object_or_404(Stagiaire, pk=pk)
    if request.method == 'POST':
        form = StagiaireForm(request.POST, instance=stagiaire)
        if form.is_valid():
            form.save()
            return redirect('liste_stagiaires')
    else:
        form = StagiaireForm(instance=stagiaire)
    return render(request, 'stagiaires/modifier_stagiaire.html', {'form': form, 'stagiaire': stagiaire})

@login_required
def supprimer_stagiaire(request, pk):
    stagiaire = get_object_or_404(Stagiaire, pk=pk)
    if request.method == 'POST':
        stagiaire.delete()
        return redirect('liste_stagiaires')
    return render(request, 'stagiaires/supprimer_stagiaire.html', {'stagiaire': stagiaire})
