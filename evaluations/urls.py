from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_evaluations, name='liste_evaluations'),
    path('ajouter/', views.ajouter_evaluation, name='ajouter_evaluation'),
    path('<int:pk>/', views.detail_evaluation, name='detail_evaluation'),
    path('<int:pk>/modifier/', views.modifier_evaluation, name='modifier_evaluation'),
    path('<int:pk>/supprimer/', views.supprimer_evaluation, name='supprimer_evaluation'),
]
