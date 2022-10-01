from django.contrib import admin
from .models.user import User
from .models.medicos import Medicos
from .models.horarios import Horarios
from .models.citas import Citas

admin.site.register(User)
admin.site.register(Medicos)
admin.site.register(Horarios)
admin.site.register(Citas)




# Register your models here.
