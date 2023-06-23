from hdbcli import dbapi
import os
from dotenv import load_dotenv
import pandas as pd
import openpyxl
from model.conectDB import conect
from components.converTextData import ConverText
from components.dataExtract import extracData
from model.modelSQL import Structure

"""
Modulo Encardo de la conexión a la base y generación del archivo de ecxel 
"""
coon = conect()
class ParrettoSend(Structure):
    """
    Se encarga de generar el objeto del provedor junto con el iventario que maneja
    """

    def __init__(self, schemeDB, 
                 wareHouse, 
                 initDate=None, 
                 endDate=None, 
                 nameCellers=None, 
                 nameHouse=None, 
                 codeHouse=None) -> None:
        super().__init__(schemeDB, wareHouse, initDate, endDate)
        self.nameCellers = nameCellers
        self.nameHouse = nameHouse
        self.codeHouse = codeHouse
    
    
    def transformData(self):
        text = ConverText.converTextFormatSQL('parrettoventas.sql', self.schemeDB)
        datas, nameRows = extracData(text)
        data = pd.array(datas)
        wb = openpyxl.Workbook()
        hoja = wb.active
        hoja.append(nameRows)
        for i in range(len(data)):
            hoja.append(list(data[i]))
        
        wb.save(os.path.join(os.path.dirname(os.path.abspath('docs')),'scripts/docs/'+self.nameArchivo()))

    def nameArchivo(self):
        return 'Parretto de Ventas.xlsx'.format(self.nameHouse)

    