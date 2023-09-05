# Blogger

>En este proyecto de blog el objetivo principal es que los usuarios puedan registrarse con un nombre y una contraseña, que al iniciar puedan escribir posteos, seleccionar la categoria a la que pertenecen y comentar los posteos que aparecen en el inicio

## Requisitos

Python
Flask
Flask-Migrate
Node.js
SQLAlchemy
Xammp

## Cómo funciona

En primer lugar, es necesario tener actualizadas las últimas versiones de las herramientas especificadas en los requisitos. 
Comenzamos por ingresar al siguiente link en GitHub para poder clonar el repositorio en nuestra computadora, de manera local: 
[repositorio](git@github.com:jbsnm/integrador_python.git)
Para hacer que funcione vamos a crear un entorno virtual en la computadora y activarlo de la siguiente manera en la terminal:

`python3 -m venv venv`

`source venv/bin/activate`

Una vez creado y activado el entorno, le intalamos las dependencias:

`pip install -r requirements.txt`

A continuación ponemos a funcionar a Xammp:

`sudo /opt/lampp/manager-linux-x64.run`

Nos queda crear, actualizar y hacer funcionar a las migraciones:

`flask db init`

`flask db migrate -m "..."`

`flask db upgrade`

Por último, iniciamos y hacemos que corra el proyecto:

`flask run`

Con el link que nos tira la consola vamos a poder acceder a la página de **blogger**
