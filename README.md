# SendEmailAutomatic
Envió de información de manera automática mediante la estración de consulta de Sap Bussiones One 
~~~
SendEmailAutomatic
│   .gitignore
│   LICENSE
│   README.md
│   requirements.txt
│   serverConfig.bash
│   setup.py
│
├───docs
└───scripts
    │   .env
    │   data.json
    │   dataGeneration.py
    │   main.py
    │   sendMail.py
    │   shippingControl.py
    │   __init__.py
    │
    ├───query
    │       Iventory.sql
    │
    ├───templates
    │       menssage.html
    │
    └───__pycache__
            dataGeneration.cpython-39.pyc
            sendMail.cpython-39.pyc
            shippingControl.cpython-39.pyc
~~~
El uso logico para el envio se observa de la siguiente forma.
![Draw](/SendEmailAutomatic/markdown/Diagrama.png)

De esta forma de uso podemos observar que se tiene una consulta  para SAP HANA, dond el modulo realiza la consulta y extrae esos datos para luego ser transformados en un Excel, Una vez se tenga el archivo se va armar el correo con el adjunto del archivo que va hacer enviado los diferentes correos de los provedores que va  estar extructurados en un archivo Json adicional va estar incluido dentro del server para ser enviado de forma programada en ciertas fechas.

## Instalación del proyecto en el server

Clonar proyecto
~~~ fihs
git clone 
~~~ 
Se crea el entorno virtual `venv`
~~~ bash
python -m venv venv
~~~
Se instalar los paquetes adicionales para el funcionamiento.
~~~ python
pip install -r requirements.txt
~~~
Tomar el bash para ser ejecutado 

## Estructura de archivos internos

Los siguientes archivos deben sercreados en la ruta `SendEmailAutomatic/scripts/`

# .env
Archivo Encargado de contener las variables de entorno con la coneción del server
~~~ env
SERVERSAP = Server.host.com
USERSAP = userDataBase
PASSWORDSAP =  PasswordDataBase
PORTSAP = 300003
PASSWORDEMAIL = emailPasswordporgmail
~~~

## JSON
Archivo de consulta para poder realizar el proceso de envio a los diferentes usuarios.

~~~ json

~~~

