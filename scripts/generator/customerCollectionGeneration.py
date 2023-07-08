from datetime import datetime
from model.conectDB import conect
from components.converTextData import ConverText
from components.dataExtract import extracData
from components.transformData import dateNowFormat
from model.modelSQL import Structure
import pandas as pd

"""
Modulo Encardo de la conexión a la base y generación del archivo de ecxel 
"""

coon = conect()
class CustomerCollectionSend(Structure):
    """
    Se encarga de generar el objeto del proveedor junto con el inventario que maneja
    """

    def __init__(self, schemeDB, 
                 initDate=None, 
                 endDate=None, 
                 nameCellers=None, 
                 nameHouse=None, 
                 codeHouse=None) -> None:
        super().__init__(schemeDB, initDate, endDate)
        self.nameCellers = nameCellers
        self.nameHouse = nameHouse
        self.codeHouse = codeHouse
    
    def date(self, ref = str):
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
        endDateCheck = str(row[5])
        wait = self.date(endDateCheck)
        coin = int(row[4])
        email = str(row[6])
        time_pay = str(row[7])

        if time_pay.find(" Días") > 0:
            time_pay = time_pay.replace(" Días","")
            time_pay = int(time_pay)
        elif time_pay.find(" Dia") > 0:
            time_pay = time_pay.replace(" Dia","")
            time_pay = int(time_pay)
        else:
            time_pay = 0

        return nameClient, ccCLient, endDateCheck, wait, coin, email, time_pay
