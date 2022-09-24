from .medicos import Medicos
from django.db import models

class Horarios (models.Model):
    id = models.BigAutoField(primary_key=True)
    id_Medico=models.ForeignKey(Medicos,related_name = "medico", on_delete=models.PROTECT)
    time = models.TimeField('hora')
