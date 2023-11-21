
import pandas as pd
import openpyxl
from components.converTextData import ConverText
from components.dataExtract import extracData, getFilePath
from model.modelSQL import Structure

class inventoryLVPsend(Structure):
    """ Modulo encargado de la generacion de archivos en base a variable establecidas"""

    def __init__(self, schemeDB, 
                 wareHouse, nameInventory,
                 initDate=None, 
                 endDate=None, 
                 nameCellers=None, 
                 nameHouse=None, 
                 codeHouse=None,
                 ) -> None:
        super().__init__(schemeDB, wareHouse, initDate, endDate)
        self.nameCellers = nameCellers
        self.nameHouse = nameHouse
        self.codeHouse = codeHouse
        self.nameInventory = nameInventory
    
    def transformData(self):
        #Procesa informacion de una consulta SQL y la transforma a Excel
        text = ConverText.converTextFormatSQL('LVPinventory.sql',self.codeHouse, self.wareHouse, self.schemeDB)
        data , description = extracData(text)
        ConverText.ConverDataXlsx(description, data, self.nameInventory)
        print(self.nameInventory)

    