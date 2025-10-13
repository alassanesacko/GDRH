from django.urls import path
from . import views

urlpatterns = [
    path('', views.liste_formations, name='liste_formations'),
    path('ajouter/', views.ajouter_formation, name='ajouter_formation'),
    path('<int:pk>/', views.detail_formation, name='detail_formation'),
    path('<int:pk>/modifier/', views.modifier_formation, name='modifier_formation'),
    path('<int:pk>/supprimer/', views.supprimer_formation, name='supprimer_formation'),
]
