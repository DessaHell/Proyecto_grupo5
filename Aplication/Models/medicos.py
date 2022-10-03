from Aplication.models.user import User
from django.db import models


class Medicos (models.Model):
    id_medico = models.BigAutoField('id_medico', primary_key=True)
    user=models.ForeignKey(User, on_delete=models.PROTECT)
    especialidad = models.CharField(max_length=20)


