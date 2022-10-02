from .medicos import Medicos
from django.db import models

class Horarios (models.Model):
    id_horario = models.BigAutoField('id_horario', primary_key=True)
    id_Medico=models.ForeignKey(Medicos, on_delete=models.PROTECT)
    time = models.TimeField('hora')
