from rest_framework import  generics
from .serializers import *
from .models import *
from rest_framework.response import Response

#AUTH imports
from rest_framework import permissions
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
# Create your views here.

#API registro de USUARIOS
class RegistroViewSet(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):

        user = UserSerializer(data=request.data)
        if user.is_valid():
            # Grab user data
            role = 'user'
            first_name = request.data['first_name']
            last_name = request.data['last_name']
            email = request.data['email']
            password = request.data['password']

            existing_user = User.objects.filter(email=email).first()

            if existing_user:
                return Response({"message": "Username "+email+", is already taken"}, 400)

            user = User.objects.create(username=email,
                                       email=email,
                                       first_name=first_name,
                                       last_name=last_name,
                                       is_active=1)

            user.save()
            user.set_password(password)
            user.save()

            group, created = Group.objects.get_or_create(name=role)
            group.user_set.add(user)
            user.save()

            # Create a profile for the user
            profile = Profiles.objects.create(user=user,
                                              matricula=request.data['matricula'],
                                              curp=request.data['curp'].upper(),
                                              rfc=request.data['rfc'].upper(),
                                              fecha_nacimiento=request.data['fecha_nacimiento'],
                                              edad=request.data['edad'],
                                              telefono=request.data['telefono'],
                                              ocupacion=request.data['ocupacion'])
            profile.save()

            return Response({"profile_created_id": profile.id}, 201)

        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)

#API datos de los TODOS los USUARIOS
class UsuariosViewSet(generics.CreateAPIView):
    #Autenticamos
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        profiles = Profiles.objects.filter(user__is_active=1).order_by('id')
        lista = ProfilesSerializer(profiles, many=True).data
        return Response(lista,200)


#API datos de los USUARIOS por ID
class SingleUserViewSet(generics.CreateAPIView):
    # Obtener usuario por ID
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(Profiles, id=request.data["id"])
        user = ProfilesSerializer(user, many=False).data

        return Response(user, 200)
    

#API modificar USUARIOS
class ModificarUsuarioViewSet(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        # iduser=request.data["id"]
        profile = get_object_or_404(Profiles, id=request.data["id"])
        profile.fecha_nacimiento = request.data["fecha_nacimiento"]
        profile.curp = request.data["curp"]
        profile.rfc = request.data["rfc"]
        profile.edad = request.data["edad"]
        profile.telefono = request.data["telefono"]
        profile.ocupacion = request.data["ocupacion"]
        profile.matricula = request.data["matricula"]
        profile.save()
        temp = profile.user
        temp.first_name = request.data["first_name"]
        temp.last_name = request.data["last_name"]
        temp.save()
        user = ProfilesSerializer(profile, many=False).data

        return Response(user, 200)

#API eliminar USUARIOS
class EliminarUsuarioViewSet(generics.CreateAPIView):
    def delete(self, request, *args, **kwargs):
        profile = get_object_or_404(Profiles, id=request.data["id"])
        try:
            profile.user.delete()
            return Response({"details": "Usuario eliminado"}, 200)
        except Exception as e:
            return Response({"details": "Algo pasó al eliminar"}, 400)


#API datos de las MATERIAS
class MateriasViewSet(generics.CreateAPIView):
    #Autenticamos
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        materia = Materia.objects.all()
        serializer = MateriaSerializer(materia, many=True)
        return Response(serializer.data)
    
    #Registrar nueva materia
    def post(self, request, *args, **kwargs):
        materia = MateriaSerializer(data=request.data)
        if materia.is_valid():
            # Cachamos los datos de la materia
            nrc = materia.data['nrc']
            nombre = materia.data['nombre']
            dias_semana = materia.data['dias_semana']
            horario_inicio = materia.data['horario_inicio']
            horario_fin = materia.data['horario_fin']
            salon = materia.data['salon']
            programa_educativo = materia.data['programa_educativo']

            # Creamos la materia
            materia = Materia(nrc=nrc, nombre=nombre, dias_semana=dias_semana, horario_inicio=horario_inicio, horario_fin=horario_fin, salon=salon, programa_educativo=programa_educativo)
            materia.save()
            return Response({"message": "Materia registrada correctamente"}, 201)
        return Response({"message": "Error al registrar la materia"}, 400)
    



    