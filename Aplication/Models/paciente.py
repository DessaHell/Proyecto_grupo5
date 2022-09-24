from Aplication.models.user import User
from django.db import models


class Paciente (models.Model):
    id = models.BigAutoField(primary_key=True)
    user=models.ForeignKey(User,related_name = "paciente",on_delete=models.PROTECT)
    phone = models.BigIntegerField('phone',max_length=15)
    city=models.CharField('city',max_length=20)