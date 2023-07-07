from hdbcli import dbapi
import os
from dotenv import load_dotenv
import pandas as pd
import openpyxl
from model.conectDB import conect
from components.converTextData import ConverText
from components.dataExtract import extracData, getFilePath
from model.modelSQL import Structure, Proveedor

"""
Modulo Encardo de la conexión a la base y generación del archivo de ecxel 
"""
coon = conect()
class ProveedoresSend(Structure):
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
        text = ConverText.converTextFormatSQL('Iventory.sql',self.codeHouse, self.wareHouse, self.schemeDB)
        datas, nameRows = extracData(text)
        data = pd.array(datas)
        Data_2 = pd.DataFrame(datas, columns= nameRows )
        wb = openpyxl.Workbook()
        hoja = wb.active
        hoja.append(nameRows)
        for i in range(len(data)):
            hoja.append(list(data[i]))
        
        hoja['R{}'.format(len(data)+2)] = Data_2['TotalUltimoPrecioCompra'].sum()
        
        wb.save(getFilePath('docs',self.nameArchivo()))

    def nameArchivo(self):
        return 'Inventario {}.xlsx'.format(self.nameHouse)

    