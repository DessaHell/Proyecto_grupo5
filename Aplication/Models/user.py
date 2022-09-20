from unittest.util import _MAX_LENGTH
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
        documento, password, self
    ):
        if not documento:
            raise ValueError("El documento es necesario")
        document = self.model(documento)
        document.set_password(password)
        document.save(using=self._db)
        return document

    def create_superuser(
        documento, password, self
    ):
        user = self.create_user(
            document=documento,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User ():
     id = models.BigAutoField(primary_key=True)
     fullName = models.CharField('Nombre', max_length=45)
     documentType = models.CharField('Tipo de Documento', max_length=50)
     document = models.BigIntegerField('Documento', max_length=50,unique=True)
     password = models.CharField('Password', max_length=20)


