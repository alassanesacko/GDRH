from django.db import models
from personnel.models import Employe

class Evaluation(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    date = models.DateField()
    note = models.IntegerField()
    commentaire = models.TextField(blank=True)

    def __str__(self):
        return f"Evaluation de {self.employe} le {self.date}"
