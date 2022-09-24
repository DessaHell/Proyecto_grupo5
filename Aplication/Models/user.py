from xml.dom.minidom import DocumentType
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.contrib.auth.hashers import make_password

# la contrase;a se va a encriptar


class UserManager(BaseUserManager):
    def create_user(
        document, password, self
    ):
        if not document:
            raise ValueError("El documento es necesario")
        user = self.model(document=document)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        document, password, self
    ):
        user = self.create_user(
            document=document,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User (AbstractBaseUser, PermissionsMixin):
     fullName = models.CharField('Nombre', max_length=45)
     documentType = models.CharField('Tipo de Documento', max_length=50)
     document = models.BigIntegerField('Documento', primary_key=True, max_length=50)
     password = models.CharField('Password', max_length=20)

     def save (self, **kwargs): #encriptar la contrasena del usuario #** los pasa como un diccionario
        some_salt = 'rGbYjM0sAe1btDxPKlw'
        self.password = make_password(self.password,some_salt) #metodo para encriptar
        super().save(**kwargs)#guardarla

     objects = UserManager() #cuando yo vaya a crear un usuario me va a llamar a la clase usermanager
     USERNAME_FIELD = 'document' #es con lo que los usuarios se van a autenticar  e ingresar



