
from django.db import models
from django.contrib.auth.models import User

class Employe(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField(null=True, blank=True)
    poste = models.CharField(max_length=100,null=True, blank=True)
    service = models.CharField(max_length=100, null=True, blank=True)
    date_embauche = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    telephone = models.CharField(max_length=20, null=True, blank=True)
    adresse = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
