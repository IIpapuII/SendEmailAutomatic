
from hdbcli import dbapi
import os
from dotenv import load_dotenv
"""
Modulo Encardo de la conexión a la base y generación del archivo de ecxel 
"""

load_dotenv()
#coneción al server  de DataBase
def conect():
    conn = dbapi.connect(
    address= os.getenv('SERVERSAP'),
    port= os.getenv('PORTSAP'),
    user= os.getenv('USERSAP'),
    password= os.getenv('PASSWORDSAP')
    )
    print("conectado")
    return conn.cursor()
