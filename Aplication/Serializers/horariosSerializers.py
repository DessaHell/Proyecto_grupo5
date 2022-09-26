from Aplication.models.horarios import Horarios
from rest_framework import serializers

class horariosSerializers (serializers.ModelSerializers):
    class Meta:
       models = Horarios
       fields = ['id', 'id_medico', 'time']
