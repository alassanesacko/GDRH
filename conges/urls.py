from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_conges, name='liste_conges'),
    path('ajouter/', views.ajouter_conge, name='ajouter_conge'),
    path('<int:pk>/', views.detail_conge, name='detail_conge'),
    path('<int:pk>/modifier/', views.modifier_conge, name='modifier_conge'),
    path('<int:pk>/supprimer/', views.supprimer_conge, name='supprimer_conge'),
]
