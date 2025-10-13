from django.shortcuts import render, redirect, get_object_or_404
from .models import Employe
from django.contrib.auth.decorators import login_required
from django import forms




class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = ['nom', 'prenom', 'date_naissance', 'poste', 'service', 'date_embauche', 'email', 'telephone', 'adresse']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'login-input'}),
            'prenom': forms.TextInput(attrs={'class': 'login-input'}),
            'date_naissance': forms.DateInput(attrs={'type': 'date', 'class': 'login-input'}),
            'poste': forms.TextInput(attrs={'class': 'login-input'}),
            'service': forms.TextInput(attrs={'class': 'login-input'}),
            'date_embauche': forms.DateInput(attrs={'type': 'date', 'class': 'login-input'}),
            'email': forms.EmailInput(attrs={'class': 'login-input'}),
            'telephone': forms.TextInput(attrs={'class': 'login-input'}),
            'adresse': forms.Textarea(attrs={'class': 'login-input'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            qs = Employe.objects.filter(email=email)
            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise forms.ValidationError("Cet email est déjà utilisé par un autre employé.")
        return email

@login_required
def liste_employes(request):
    if request.user.groups.filter(name='DRH').exists():
        employes = Employe.objects.all()
    else:
        employes = Employe.objects.filter(user=request.user)
    return render(request, 'personnel/liste_employes.html', {'employes': employes})

@login_required
def ajouter_employe(request):
    if not request.user.groups.filter(name='DRH').exists():
        return redirect('liste_employes')
    if request.method == 'POST':
        form = EmployeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_employes')
    else:
        form = EmployeForm()
    return render(request, 'personnel/ajouter_employe.html', {'form': form})

@login_required
def detail_employe(request, pk):
    employe = get_object_or_404(Employe, pk=pk)
    # Seul le DRH ou l'employé concerné peut voir la fiche
    if not request.user.groups.filter(name='DRH').exists() and employe.user != request.user:
        return redirect('liste_employes')
    return render(request, 'personnel/detail_employe.html', {'employe': employe})

@login_required
def modifier_employe(request, pk):
    if not request.user.groups.filter(name='DRH').exists():
        return redirect('liste_employes')
    employe = get_object_or_404(Employe, pk=pk)
    if request.method == 'POST':
        form = EmployeForm(request.POST, instance=employe)
        if form.is_valid():
            form.save()
            return redirect('liste_employes')
    else:
        form = EmployeForm(instance=employe)
    return render(request, 'personnel/modifier_employe.html', {'form': form, 'employe': employe})

@login_required
def supprimer_employe(request, pk):
    if not request.user.groups.filter(name='DRH').exists():
        return redirect('liste_employes')
    employe = get_object_or_404(Employe, pk=pk)
    if request.method == 'POST':
        employe.delete()
        return redirect('liste_employes')
    return render(request, 'personnel/supprimer_employe.html', {'employe': employe})
