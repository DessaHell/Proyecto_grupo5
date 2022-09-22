from Aplication.Models.citas import Citas
from rest_framework import serializers


class citasSerializers (serializers.ModelSerializers):
    class Meta:
       models = Citas
       fields = ['id','fecha']