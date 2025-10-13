from django.db import models
from personnel.models import Employe

class Formation(models.Model):
    titre = models.CharField(max_length=100)
    employes = models.ManyToManyField(Employe, related_name='formations')
    date_debut = models.DateField()
    date_fin = models.DateField()
    organisme = models.CharField(max_length=100)

    def __str__(self):
        return self.titre
