from django.db import models

class Stagiaire(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20)
    ecole = models.CharField(max_length=100)
    date_debut = models.DateField()
    date_fin = models.DateField()
    sujet = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
