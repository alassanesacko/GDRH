from django.db import models
from personnel.models import Employe

class FichePaie(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    mois = models.CharField(max_length=20)
    annee = models.IntegerField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_versement = models.DateField()

    def __str__(self):
        return f"Paie {self.mois}/{self.annee} - {self.employe}"
