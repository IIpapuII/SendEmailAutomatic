from datetime import datetime
from components.converTextData import ConverText
from components.dataExtract import extracData
from model.modelSQL import Structure

"""
Modulo Encardo de la conexión a la base y generación del archivo de ecxel 
"""

class CustomerCollectionSend(Structure):
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
        formatted_ref_array = str(ref_array).replace("[","").replace("]","")
        text = ConverText.converTextFormatSQL('customerCollection.sql', self.schemeDB, formatted_ref_array)
        datas, nameRows = extracData(text)
        row = datas[len(datas)-1]

        nameClient = str(row[1])
        ccCLient = str(row[2])
        coin = int(row[4])
        endDateCheck = str(row[5])
        wait = self.date(endDateCheck)
        email = str(row[6])

        return nameClient, ccCLient, endDateCheck, wait, coin, email