from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_stagiaires, name='liste_stagiaires'),
    path('ajouter/', views.ajouter_stagiaire, name='ajouter_stagiaire'),
    path('<int:pk>/', views.detail_stagiaire, name='detail_stagiaire'),
    path('<int:pk>/modifier/', views.modifier_stagiaire, name='modifier_stagiaire'),
    path('<int:pk>/supprimer/', views.supprimer_stagiaire, name='supprimer_stagiaire'),
]
