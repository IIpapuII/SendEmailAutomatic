from datetime import datetime
from components.converTextData import ConverText
from components.dataExtract import extracData
from model.modelSQL import Structure

"""
Modulo Encardo de la conexión a la base y generación del archivo de ecxel 
"""

class SendMessageClients(Structure):
    """
    Se encarga de generar el objeto del proveedor junto con el inventario que maneja
    """
    def __init__(self, schemeDB):
        self.schemeDB = schemeDB
    
    def date(self, ref: str):
        fecha1 = datetime.strptime(ref, '%d/%m/%Y')
        fecha1.strftime('%d/%m/%Y')
        fecha2 = datetime.now()
        fecha2.strftime('%d/%m/%Y')

        fecha_diferencia = fecha2 - fecha1
        return fecha_diferencia.days

    def transformData(self, ref_array): 
        text = ConverText.converTextFormatSQL('SendMessageClients.sql', self.schemeDB, ref_array)
        datas, nameRows = extracData(text)

        row = datas[0]

        cn = str(row[0])
        name = str(row[1])
        email = str(row[2])

        return cn, name, email