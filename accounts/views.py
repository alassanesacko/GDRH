
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.groups.filter(name='DRH').exists():
                return redirect('dashboard_drh')
            else:
                return redirect('dashboard_employe')
        else:
            return render(request, 'accounts/login.html', {'error': "Nom d'utilisateur ou mot de passe incorrect."})
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            from personnel.models import Employe
            # Vérifie que l'email n'existe pas déjà
            if not Employe.objects.filter(email=user.email).exists():
                Employe.objects.create(
                    user=user,
                    nom=user.last_name or user.username,
                    prenom=user.first_name or '',
                    email=user.email
                )
            login(request, user)
            return redirect('dashboard_employe')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

@login_required
def dashboard_drh(request):
    return render(request, 'accounts/dashboard_drh.html')

@login_required

def dashboard_employe(request):
    return render(request, 'accounts/dashboard_employe.html')

@login_required
def employe_profil(request):
    employe = None
    try:
        employe = request.user.employe
    except Exception:
        pass
    return render(request, 'accounts/employe_profil.html', {
        'user': request.user,
        'employe': employe
    })

@login_required

def employe_completer_profil(request):
    from personnel.models import Employe
    from personnel.views import EmployeForm
    from django.db import IntegrityError
    # Vérifie que l'email n'existe pas déjà pour un autre Employe
    employe = None
    try:
        employe = Employe.objects.get(user=request.user)
    except Employe.DoesNotExist:
        if not Employe.objects.filter(email=request.user.email).exists():
            employe = Employe.objects.create(
                user=request.user,
                nom=request.user.last_name or request.user.username,
                prenom=request.user.first_name or '',
                email=request.user.email
            )
        else:
            employe = Employe.objects.create(
                user=request.user,
                nom=request.user.last_name or request.user.username,
                prenom=request.user.first_name or '',
                email=None
            )
    error_message = None
    if request.method == 'POST':
        form = EmployeForm(request.POST, instance=employe)
        if form.is_valid():
            try:
                form.save()
                return redirect('employe_profil')
            except IntegrityError:
                error_message = "Cet email est déjà utilisé par un autre employé."
        # Si le formulaire n'est pas valide, les erreurs seront affichées normalement
    else:
        form = EmployeForm(instance=employe)
    return render(request, 'personnel/completer_profil.html', {'form': form, 'error_message': error_message})

def employe_conges(request):
    return render(request, 'accounts/employe_conges.html')

@login_required
def employe_contrats(request):
    return render(request, 'accounts/employe_contrats.html')

@login_required
def employe_evaluations(request):
    return render(request, 'accounts/employe_evaluations.html')

@login_required
def employe_formations(request):
    return render(request, 'accounts/employe_formations.html')

@login_required
def employe_paie(request):
    return render(request, 'accounts/employe_paie.html')
