from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_fiches_paie, name='liste_fiches_paie'),
    path('ajouter/', views.ajouter_fiche_paie, name='ajouter_fiche_paie'),
    path('<int:pk>/', views.detail_fiche_paie, name='detail_fiche_paie'),
    path('<int:pk>/modifier/', views.modifier_fiche_paie, name='modifier_fiche_paie'),
    path('<int:pk>/supprimer/', views.supprimer_fiche_paie, name='supprimer_fiche_paie'),
]
