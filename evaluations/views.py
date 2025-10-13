from django.shortcuts import render, redirect, get_object_or_404
from .models import Evaluation
from personnel.models import Employe
from django.contrib.auth.decorators import login_required
from django import forms

class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = ['employe', 'date', 'note', 'commentaire']

@login_required
def liste_evaluations(request):
    evaluations = Evaluation.objects.all()
    return render(request, 'evaluations/liste_evaluations.html', {'evaluations': evaluations})

@login_required
def ajouter_evaluation(request):
    if request.method == 'POST':
        form = EvaluationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_evaluations')
    else:
        form = EvaluationForm()
    return render(request, 'evaluations/ajouter_evaluation.html', {'form': form})

@login_required
def detail_evaluation(request, pk):
    evaluation = get_object_or_404(Evaluation, pk=pk)
    return render(request, 'evaluations/detail_evaluation.html', {'evaluation': evaluation})

@login_required
def modifier_evaluation(request, pk):
    evaluation = get_object_or_404(Evaluation, pk=pk)
    if request.method == 'POST':
        form = EvaluationForm(request.POST, instance=evaluation)
        if form.is_valid():
            form.save()
            return redirect('liste_evaluations')
    else:
        form = EvaluationForm(instance=evaluation)
    return render(request, 'evaluations/modifier_evaluation.html', {'form': form, 'evaluation': evaluation})

@login_required
def supprimer_evaluation(request, pk):
    evaluation = get_object_or_404(Evaluation, pk=pk)
    if request.method == 'POST':
        evaluation.delete()
        return redirect('liste_evaluations')
    return render(request, 'evaluations/supprimer_evaluation.html', {'evaluation': evaluation})
