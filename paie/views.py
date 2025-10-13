from django.shortcuts import render, redirect, get_object_or_404
from .models import FichePaie
from personnel.models import Employe
from django.contrib.auth.decorators import login_required
from django import forms

class FichePaieForm(forms.ModelForm):
    class Meta:
        model = FichePaie
        fields = ['employe', 'mois', 'annee', 'montant', 'date_versement']

@login_required
def liste_fiches_paie(request):
    fiches = FichePaie.objects.all()
    return render(request, 'paie/liste_fiches_paie.html', {'fiches': fiches})

@login_required
def ajouter_fiche_paie(request):
    if request.method == 'POST':
        form = FichePaieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_fiches_paie')
    else:
        form = FichePaieForm()
    return render(request, 'paie/ajouter_fiche_paie.html', {'form': form})

@login_required
def detail_fiche_paie(request, pk):
    fiche = get_object_or_404(FichePaie, pk=pk)
    return render(request, 'paie/detail_fiche_paie.html', {'fiche': fiche})

@login_required
def modifier_fiche_paie(request, pk):
    fiche = get_object_or_404(FichePaie, pk=pk)
    if request.method == 'POST':
        form = FichePaieForm(request.POST, instance=fiche)
        if form.is_valid():
            form.save()
            return redirect('liste_fiches_paie')
    else:
        form = FichePaieForm(instance=fiche)
    return render(request, 'paie/modifier_fiche_paie.html', {'form': form, 'fiche': fiche})

@login_required
def supprimer_fiche_paie(request, pk):
    fiche = get_object_or_404(FichePaie, pk=pk)
    if request.method == 'POST':
        fiche.delete()
        return redirect('liste_fiches_paie')
    return render(request, 'paie/supprimer_fiche_paie.html', {'fiche': fiche})
