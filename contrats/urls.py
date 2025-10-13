from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_contrats, name='liste_contrats'),
    path('ajouter/', views.ajouter_contrat, name='ajouter_contrat'),
    path('<int:pk>/', views.detail_contrat, name='detail_contrat'),
    path('<int:pk>/modifier/', views.modifier_contrat, name='modifier_contrat'),
    path('<int:pk>/supprimer/', views.supprimer_contrat, name='supprimer_contrat'),
]
