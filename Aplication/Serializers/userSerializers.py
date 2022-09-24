from dataclasses import fields
from xml.dom.minidom import Document
from Aplication.models.citas import Citas
from Aplication.models.horarios import Horarios
from Aplication.models.medicos import Medicos
from Aplication.models.paciente import Paciente
from Aplication.models.user import User

from rest_framework import serializers
from .userSerializers import userSerializers

class UserSerializer(serializers.ModelSerializer):
    account = userSerializers()
    class Meta:
        model = User
        fields =['id','fullName','password','documentType','document']

    def create(self, data): #DESERIALIZACIÓN
        userData = data.pop('account')
        userInstance = User.objects.create(**data)
        User.objects.create(**userData, user = userInstance)