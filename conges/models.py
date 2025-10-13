from django.db import models
from personnel.models import Employe

class Conge(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField()
    motif = models.CharField(max_length=255)
    statut = models.CharField(max_length=50, choices=[('En attente', 'En attente'), ('Validé', 'Validé'), ('Refusé', 'Refusé')], default='En attente')

    def __str__(self):
        return f"Congé de {self.employe} du {self.date_debut} au {self.date_fin}"
