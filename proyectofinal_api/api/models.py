from django.db import models
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import  User



class BearerTokenAuthentication(TokenAuthentication):
    keyword = u"Bearer"

class Profiles(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, default=None)
    matricula = models.CharField(max_length=255,null=True, blank=True)
    curp = models.CharField(max_length=255,null=True, blank=True)
    rfc = models.CharField(max_length=255,null=True, blank=True)
    #fecha_nacimiento = models.CharField(max_length=255,null=True, blank=True)
    fecha_nacimiento = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    telefono = models.CharField(max_length=255, null=True, blank=True)
    ocupacion = models.CharField(max_length=255,null=True, blank=True)
    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "Perfil del usuario "+self.user.first_name+" "+self.user.last_name

class Materia(models.Model):
    id = models.BigAutoField(primary_key=True)
    nrc = models.CharField(max_length=255,null=True, blank=True)
    nombre = models.CharField(max_length=255,null=True, blank=True)
    dias_semana = models.CharField(max_length=255,null=True, blank=True)
    horario_inicio = models.TimeField(null=True, blank=True)
    horario_fin = models.TimeField(null=True, blank=True)
    salon = models.CharField(max_length=255,null=True, blank=True)
    programa_educativo = models.CharField(max_length=255,null=True, blank=True)

    creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    update = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "Materia :"+self.nombre + " NRC: "+self.nrc 