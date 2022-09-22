from Aplication.Models.medicos import Medicos
from rest_framework import serializers


class medicosSerializers (serializers.ModelSerializers):
    class Meta:
       models = Medicos
       fields = ['id','especialidad']