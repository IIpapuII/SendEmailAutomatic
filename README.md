# SendEmailAutomatic
Envió de información de manera automática mediante la estración de consulta de Sap Bussiones One 
~~~
└── SendEmailAutomatic
    ├── LICENSE
    ├── markdown
    │   └── Diagrama.png
    ├── README.md
    ├── requirements.txt
    ├── scripts
    │   ├── components
    │   │   ├── converTextData.py
    │   │   ├── dataExtract.py
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   ├── converTextData.cpython-311.pyc
    │   │   │   ├── dataExtract.cpython-311.pyc
    │   │   │   ├── __init__.cpython-311.pyc
    │   │   │   ├── __init__.cpython-39.pyc
    │   │   │   ├── sendMail.cpython-311.pyc
    │   │   │   ├── sendMail.cpython-39.pyc
    │   │   │   └── transformData.cpython-311.pyc
    │   │   ├── sendMail.py
    │   │   └── transformData.py
    │   ├── config
    │   │   ├── client.json
    │   │   ├── counter.json
    │   │   ├── data.json
    │   │   └── icomessend.json
    │   ├── controller
    │   │   ├── icomeController.py
    │   │   ├── __init__.py
    │   │   ├── __pycache__
    │   │   │   ├── icomeController.cpython-311.pyc
    │   │   │   ├── __init__.cpython-311.pyc
    │   │   │   ├── __init__.cpython-39.pyc
    │   │   │   ├── shippingControl.cpython-311.pyc
    │   │   │   ├── shippingControl.cpython-39.pyc
    │   │   │   ├── shippingCustomerCollection.cpython-311.pyc
    │   │   │   ├── shippingParretto.cpython-311.pyc
    │   │   │   └── shippingSeries.cpython-311.pyc
    │   │   ├── shippingControl.py
    │   │   ├── shippingCustomerCollection.py
    │   │   ├── shippingParretto.py
    │   │   └── shippingSeries.py
    │   ├── docs
    │   │   └── Iventario UNILEVER ANDINA COLOMBIA LTDAss.xlsx
    │   ├── generator
    │   │   ├── a.py
    │   │   ├── customerCollectionGeneration.py
    │   │   ├── dataGeneration.py
    │   │   ├── generateCustomerCollection.py
    │   │   ├── generateParretto.py
    │   │   ├── generateSeries.py
    │   │   ├── icomeGenerateDate.py
    │   │   ├── __init__.py
    │   │   ├── parrettoGeneration.py
    │   │   ├── __pycache__
    │   │   │   ├── customerCollectionGeneration.cpython-311.pyc
    │   │   │   ├── dataGeneration.cpython-311.pyc
    │   │   │   ├── icomeGenerateDate.cpython-311.pyc
    │   │   │   ├── __init__.cpython-311.pyc
    │   │   │   ├── parrettoGeneration.cpython-311.pyc
    │   │   │   └── seriesGeneration.cpython-311.pyc
    │   │   └── seriesGeneration.py
    │   ├── __init__.py
    │   ├── main.py
    │   ├── model
    │   │   ├── conectDB.py
    │   │   ├── __init__.py
    │   │   ├── modelSQL.py
    │   │   └── __pycache__
    │   │       ├── conectDB.cpython-311.pyc
    │   │       ├── __init__.cpython-311.pyc
    │   │       └── modelSQL.cpython-311.pyc
    │   ├── query
    │   │   ├── customerCollection.sql
    │   │   ├── income.sql
    │   │   ├── Iventory.sql
    │   │   ├── parrettoventas.sql
    │   │   └── seriesInvoice.sql
    │   └── templates
    │       ├── customerCollection.html
    │       ├── goodsReceipt.html
    │       ├── logo (1).png
    │       ├── massiveParretto.html
    │       ├── menssage.html
    │       └── seriesNotification.html
    ├── serverConfig.bash
    └── setup.py
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

Los siguientes archivos deben sercreados en la ruta `/SendEmailAutomatic/scripts/`

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
{
    "KIMBERLY-ICH": {
        "sender" : "remitente@gmail.com",
        "addresse" : ["enviadoOne@gmail.com","EnviadoTwo@gmail.com"],
        "codeCellers": "007,050,08",
        "nameHouse": "KIMBERLY-ICH",
        "nameCellers" : "-PRINCIPAL CUCUTA<br> -AVERIAS         CUCUTA<br> -> Se comparte inventario de averías con el fin de tener su apoyo con la pronta solución.<br> -CUCUTA MNM-TAT <br>",
        "ShemeDB" : "HBTESQUEMAdb" ,
        "codeHouse" : 147 
    }
}
~~~
Se debe serguir la siguiente estrucutura para agregar un nuevo provedor y en addresse se pueden agregar la cantidad de correos que deben recibir a información. 

