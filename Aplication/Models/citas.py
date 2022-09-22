from .medicos import Medicos
from .paciente import Paciente
from .horarios import Horarios
from .user import User
from django.db import models


class Citas (models.Model):
    id = models.BigAutoField(primary_key=True)
    id_User=models.ForeignKey(User,related_name='usuario', on_delete=models.CASCADE)
    id_Medico=models.ForeignKey(Medicos,related_name = "medico")
    id_Paciente=models.ForeignKey(Paciente,related_name = "paciente")
    fecha =models.DateField('fecha')
    id_horario = models.ForeignKey(Horarios,related_name = "horarios")


