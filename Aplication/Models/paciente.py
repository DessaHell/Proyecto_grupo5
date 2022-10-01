from aplication.models.user import User
from django.db import models


class Paciente (models.Model):
    id_paciente = models.BigAutoField('id_paciente', primary_key=True)
    user=models.ForeignKey(User, on_delete=models.PROTECT)
    phone = models.CharField('phone', max_length=20)
    city=models.CharField('city', max_length=20)