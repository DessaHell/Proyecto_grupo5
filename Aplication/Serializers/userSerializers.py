from Aplication.models.user import User

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['fullName', 'documentType', 'document', 'password']

    def create(self, data): #DESERIALIZACIÓN
        userData = data
        userInstance = User.objects.create(**data)
        return userInstance


    def to_representation(self, obj):
        user = User.objects.get(document = obj.document)
        return {
            'fullName':user.fullName,
            'documentType': user.documentType,
            'document': user.document,
            'password': user.password
        }
