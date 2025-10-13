from django.shortcuts import render, redirect, get_object_or_404
from .models import Conge
from personnel.models import Employe
from django.contrib.auth.decorators import login_required
from django import forms

class CongeForm(forms.ModelForm):
    class Meta:
        model = Conge
        fields = ['employe', 'date_debut', 'date_fin', 'motif', 'statut']

@login_required
def liste_conges(request):
    conges = Conge.objects.all()
    return render(request, 'conges/liste_conges.html', {'conges': conges})

@login_required
def ajouter_conge(request):
    if request.method == 'POST':
        form = CongeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_conges')
    else:
        form = CongeForm()
    return render(request, 'conges/ajouter_conge.html', {'form': form})

@login_required
def detail_conge(request, pk):
    conge = get_object_or_404(Conge, pk=pk)
    return render(request, 'conges/detail_conge.html', {'conge': conge})

@login_required
def modifier_conge(request, pk):
    conge = get_object_or_404(Conge, pk=pk)
    if request.method == 'POST':
        form = CongeForm(request.POST, instance=conge)
        if form.is_valid():
            form.save()
            return redirect('liste_conges')
    else:
        form = CongeForm(instance=conge)
    return render(request, 'conges/modifier_conge.html', {'form': form, 'conge': conge})

@login_required
def supprimer_conge(request, pk):
    conge = get_object_or_404(Conge, pk=pk)
    if request.method == 'POST':
        conge.delete()
        return redirect('liste_conges')
    return render(request, 'conges/supprimer_conge.html', {'conge': conge})
