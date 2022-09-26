from .medicos import Medicos
from .paciente import Paciente
from .horarios import Horarios
from .user import User
from django.db import models


class Citas (models.Model):
    id = models.BigAutoField(primary_key=True)
    id_User=models.ForeignKey(User, on_delete=models.CASCADE)
    id_Medico=models.ForeignKey(Medicos, on_delete=models.CASCADE)
    id_Paciente=models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha =models.DateField('fecha')
    id_horario = models.ForeignKey(Horarios, on_delete=models.CASCADE)


