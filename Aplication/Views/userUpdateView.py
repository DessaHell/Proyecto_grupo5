from cmath import log
from django.shortcuts import get_object_or_404
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from Aplication.Serializers.userSerializers import UserSerializer
from Aplication.models.user import User

class UserUpdateView(views.APIView):
    def post(self, request, *args, **kwargs):
        ##userObject = UserSerializer(data = request.data)

        user_instance = get_object_or_404(User, pk=request.data["document"])

        if request.data.get("city") != None:
            user_instance.city = request.data["city"]

        if request.data.get("phone") != None:
            user_instance.phone = request.data["phone"]

        if request.data.get("mail") != None:
            user_instance.mail = request.data["mail"]
        
        if request.data.get("password") != None:
            user_instance.password = request.data["password"]

        user_instance.save()

        user_rep = UserSerializer.to_representation(self, user_instance)

        #user_response = User.objects.get(document = request.data["document"])
        return Response(user_rep, status=status.HTTP_201_CREATED)

