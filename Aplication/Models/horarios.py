from .medicos import Medicos
from django.db import models

class Horarios (models.Model):
    id = models.BigAutoField(primary_key=True)
    id_Medico=models.ForeignKey(Medicos,related_name = "medico")
    time = models.TimeField('hora')
