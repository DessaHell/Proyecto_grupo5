from cmath import log
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from aplication.serializers.userSerializers import UserSerializer
from aplication.models.user import User

class UserCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {"document": request.data["document"],
                     "password": request.data["password"]}
        tokens = TokenObtainPairSerializer(data = tokenData)
        tokens.is_valid(raise_exception=True)

        #user_response = User.objects.get(document = request.data["document"])
        
        return Response(tokens.validated_data, status=status.HTTP_201_CREATED)

