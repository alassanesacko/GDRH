from django.shortcuts import render, redirect, get_object_or_404
from .models import Contrat
from personnel.models import Employe
from django.contrib.auth.decorators import login_required
from django import forms

class ContratForm(forms.ModelForm):
    class Meta:
        model = Contrat
        fields = ['employe', 'type_contrat', 'date_debut', 'date_fin', 'salaire']

@login_required
def liste_contrats(request):
    contrats = Contrat.objects.all()
    return render(request, 'contrats/liste_contrats.html', {'contrats': contrats})

@login_required
def ajouter_contrat(request):
    if request.method == 'POST':
        form = ContratForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_contrats')
    else:
        form = ContratForm()
    return render(request, 'contrats/ajouter_contrat.html', {'form': form})

@login_required
def detail_contrat(request, pk):
    contrat = get_object_or_404(Contrat, pk=pk)
    return render(request, 'contrats/detail_contrat.html', {'contrat': contrat})

@login_required
def modifier_contrat(request, pk):
    contrat = get_object_or_404(Contrat, pk=pk)
    if request.method == 'POST':
        form = ContratForm(request.POST, instance=contrat)
        if form.is_valid():
            form.save()
            return redirect('liste_contrats')
    else:
        form = ContratForm(instance=contrat)
    return render(request, 'contrats/modifier_contrat.html', {'form': form, 'contrat': contrat})

@login_required
def supprimer_contrat(request, pk):
    contrat = get_object_or_404(Contrat, pk=pk)
    if request.method == 'POST':
        contrat.delete()
        return redirect('liste_contrats')
    return render(request, 'contrats/supprimer_contrat.html', {'contrat': contrat})
