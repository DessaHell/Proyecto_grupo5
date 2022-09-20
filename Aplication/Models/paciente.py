from Aplication.Models.user import User
from django.db import models


class Paciente (models.Model):
    id = models.BigAutoField(primary_key=True)
    user=models.ForeignKey(User,related_name = "paciente")
    phone = models.BigIntegerField('phone',max_length=15)
    city=models.CharField('city',max_length=20)