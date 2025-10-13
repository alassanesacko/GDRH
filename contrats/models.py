from django.db import models
from personnel.models import Employe

class Contrat(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    type_contrat = models.CharField(max_length=50)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    salaire = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Contrat {self.type_contrat} de {self.employe}"
