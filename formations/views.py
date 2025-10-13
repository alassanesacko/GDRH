from django.shortcuts import render, redirect, get_object_or_404
from .models import Formation
from personnel.models import Employe
from django.contrib.auth.decorators import login_required
from django import forms

class FormationForm(forms.ModelForm):
    class Meta:
        model = Formation
        fields = ['titre', 'employes', 'date_debut', 'date_fin', 'organisme']

@login_required
def liste_formations(request):
    formations = Formation.objects.all()
    return render(request, 'formations/liste_formations.html', {'formations': formations})

@login_required
def ajouter_formation(request):
    if request.method == 'POST':
        form = FormationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_formations')
    else:
        form = FormationForm()
    return render(request, 'formations/ajouter_formation.html', {'form': form})

@login_required
def detail_formation(request, pk):
    formation = get_object_or_404(Formation, pk=pk)
    return render(request, 'formations/detail_formation.html', {'formation': formation})

@login_required
def modifier_formation(request, pk):
    formation = get_object_or_404(Formation, pk=pk)
    if request.method == 'POST':
        form = FormationForm(request.POST, instance=formation)
        if form.is_valid():
            form.save()
            return redirect('liste_formations')
    else:
        form = FormationForm(instance=formation)
    return render(request, 'formations/modifier_formation.html', {'form': form, 'formation': formation})

@login_required
def supprimer_formation(request, pk):
    formation = get_object_or_404(Formation, pk=pk)
    if request.method == 'POST':
        formation.delete()
        return redirect('liste_formations')
    return render(request, 'formations/supprimer_formation.html', {'formation': formation})
