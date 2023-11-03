
# App Web Fullstack - MySQL, Django, Angular, Docker

Bienvenido a mi repositorio, aquí encontrarás el código fuente ejemplo para una aplicación fullstack con las tecnologías listadas.



## Instalación y ejecución

Para poder probar el proyecto necesitas crear primero un entorno virtual de Pyton e instalar las dependencias desde el archivo "requirements.txt".

```bash
    $ python -m venv venv
    $ ./venv/Scripts/activate
    $ (env) pip install -r requirements.txt
```

Además, por motivos de seguridad, el proyecto viene sin la llave secreta de Django  por lo tanto tendrás que generar una nueva llave de la siguiente manera:
```bash
    $ (env) $ python manage.py shell
    >>> from django.core.management.utils import get_random_secret_key
    >>> print(get_random_secret_key())
```

Una vez el metodo devuelva la llave, pegarla en el **"settings.py"** en el esquema **SECRET_KEY**.

No olvidemos que el proyecto tiene credenciales genericas como:

- username: root
- password: password

Por lo tanto queda a tu criterio cambiar los parámetros de la base de datos, credenciales de Django, etc...


    
## Documentation

[Tutorial y documentación](https://pinola.notion.site/Construyendo-una-App-Web-con-Docker-MySQL-Django-y-Angular-e83fbbab72bb4da19858445c7a36f7a1?pvs=4)


## Tech Stack
**Contenerización**: Docker

**Base de datos:** MySQL

**Herramientas de administración**: phpMyAdmin

**Server:** Node

**Frontend**: Angular

**Backend**: Django


## Soporte

Para más ayuda ponerse en contacto conmigo por: angel.gonzalezpi@alumno.buap.mx

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/agpineda/)


## Licencia


[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)


![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white) 

![MySQL](https://img.shields.io/badge/MySQL-00000F?style=for-the-badge&logo=mysql&logoColor=white)

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

![Angular](https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white)
