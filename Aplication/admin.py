from django.contrib import admin
from .Models.user import User
from .Models.paciente import Paciente
from .Models.medicos import Medicos
from .Models.horarios import Horarios
from .Models.citas import Citas

admin.site.register(User)
admin.site.register(Paciente)
admin.site.register(Medicos)
admin.site.register(Horarios)
admin.site.register(Citas)




# Register your models here.
