from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from Aplication.Serializers.userSerializers import UserSerializer

class UserCreateView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        tokenData = {"document": request.data["document"],
                     "password": request.data["password"]}
        tokens = TokenObtainPairSerializer(data = tokenData)
        tokens.is_valid(raise_exception=True)
        
        return Response(tokens.validated_data, status=status.HTTP_201_CREATED)

