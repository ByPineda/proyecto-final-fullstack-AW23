from django.contrib import admin
from django.urls import path, include
from api.views import *
from api.serializers import *
from api.models import *

#AUTH imports
from api.tools.auth import *

#DEBUG
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    #APP API
    #path('admin/', admin.site.urls),

    #Autenticacion
    ##----------------------------------------------------------
    path('login/', CustomAuthToken.as_view()),
    path('logout/', Logout.as_view()),
    ##----------------------------------------------------------

    #API's para obtener datos
    ##Requieren autenticacion-----------------------------------
    #Materias
    path('courses/', MateriasViewSet.as_view()),
    #Usuario Individual
    path('users/',SingleUserViewSet.as_view()),
    #Usuarios
    path('users/list', UsuariosViewSet.as_view()),
    #Modificar Usuario
    path('users/modify', ModificarUsuarioViewSet.as_view()),
    #Eliminar Usuario
    path('users/delete', EliminarUsuarioViewSet.as_view()),
    ##----------------------------------------------------------

    ##No requieren autenticacion---------------------------------
    path('users/register', RegistroViewSet.as_view()),
    ##-----------------------------------------------------------

    #DEBUG
    #path('test/', obtain_auth_token),
]
