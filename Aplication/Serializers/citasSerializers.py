from Aplication.models.citas import Citas
from rest_framework import serializers


class citasSerializers (serializers.ModelSerializers):
    class Meta:
       models = Citas
       fields = ['id_cita', 'id_usuario', 'id_medico', 'fecha', 'id_horario']