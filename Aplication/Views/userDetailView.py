from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
from django.conf import settings
from aplication.models.user import User
from aplication.serializers.userSerializers import UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs,):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]   #BEARER f6f6f7f8g6d8 (7 espacios 6 de la palabra BEARER y 1 del espacio).
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token, verify=False)

        if valid_data['document'] != str(kwargs['pk']):
            stringResponse = {'detail':'No está autorizado para realizar la petición'}
            return Response (stringResponse, status = status.HTTP_401_UNAUTHORIZED)
        
        return super().get(request, *args, **kwargs)
        