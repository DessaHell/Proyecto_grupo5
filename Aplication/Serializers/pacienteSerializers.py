from Aplication.models.paciente import Paciente
from rest_framework import serializers

class pacienteSerializers (serializers.ModelSerializers):
    class Meta:
        models = Paciente
        fields = ['id','phone', 'city']