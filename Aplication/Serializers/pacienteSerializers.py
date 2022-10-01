from aplication.models.paciente import Paciente
from rest_framework import serializers

from aplication.models.user import User

class pacienteSerializers (serializers.ModelSerializers):
    class Meta:
        models = Paciente
        fields = ['id', 'user', 'phone', 'city']

    def create(self, data): #DESERIALIZACIÓN
        userData = data.user
        pacienteData = data.pop("user")
        userInstance = User.objects.create(**userData)
        PacienteInstance = Paciente.objects.create(**pacienteData)
        PacienteInstance.user = userInstance
        return PacienteInstance


    def to_representation(self, obj):
        paciente = Paciente.objects.get(id = obj.id)
        user = paciente.user
        return {
            'fullName':paciente.fullName,
            'documentType': paciente.documentType,
            'document': paciente.document,
            'password': paciente.password,
            'user': user
        }