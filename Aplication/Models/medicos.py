from Aplication.models.user import User
from django.db import models


class Medicos (models.Model):
    id = models.BigAutoField(primary_key=True)
user=models.ForeignKey(User,related_name = "medico",on_delete=models.PROTECT)
especialidad = models.CharField(max_length=20)


