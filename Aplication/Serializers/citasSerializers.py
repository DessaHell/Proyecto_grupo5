from Aplication.models.citas import Citas
from rest_framework import serializers


class citasSerializers (serializers.ModelSerializers):
    class Meta:
       models = Citas
       fields = ['id', 'id_User', 'id_Medico', 'id_Paciente', 'fecha', 'id_horario']