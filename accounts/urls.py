from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard-drh/', views.dashboard_drh, name='dashboard_drh'),
    # ...existing code...
    path('dashboard-employe/', views.dashboard_employe, name='dashboard_employe'),
    path('employe/profil/', views.employe_profil, name='employe_profil'),
    path('employe/completer-profil/', views.employe_completer_profil, name='employe_completer_profil'),
    path('employe/conges/', views.employe_conges, name='employe_conges'),
    path('employe/contrats/', views.employe_contrats, name='employe_contrats'),
    path('employe/evaluations/', views.employe_evaluations, name='employe_evaluations'),
    path('employe/formations/', views.employe_formations, name='employe_formations'),
    path('employe/paie/', views.employe_paie, name='employe_paie'),
]
