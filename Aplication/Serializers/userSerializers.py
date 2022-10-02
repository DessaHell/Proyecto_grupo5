from aplication.models.user import User

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['fullName', 'documentType', 'document', 'password', 'phone', 'city', 'mail']

    def create(self, data): #DESERIALIZACIÓN
        userData = data.user
        userInstance = User.objects.create(**data)
        return userInstance


    def to_representation(self, obj):
        user = User.objects.get(document = obj.document)
        return {
            'fullName':user.fullName,
            'documentType': user.documentType,
            'document': user.document,
            'password': user.password,
            'phone': user.phone,
            'mail': user.mail,
            'city': user.city
        }
