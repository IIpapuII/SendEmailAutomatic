from components.converTextData import ConverText
from components.dataExtract import extracData
from model.modelSQL import Structure
from datetime import date, timedelta
import calendar

class inventoryLVPsend(Structure):
    """ Modulo encargado de la generacion de archivos en base a variable establecidas"""

    def __init__(self, schemeDB, 
                 wareHouse, nameInventory,
                 nameCellers=None, 
                 nameHouse=None, 
                 codeHouse=None,
                 ) -> None:
        super().__init__(schemeDB, wareHouse)
        self.nameCellers = nameCellers
        self.nameHouse = nameHouse
        self.codeHouse = codeHouse
        self.nameInventory = nameInventory
    
    def transformData(self):
        #Procesa informacion de una consulta SQL y la transforma a Excel
        day_int = date.today().day
        day_str = calendar.day_name[date.today().weekday()]

        # if day_int == 1:        #Si es el primer dia del mes; arrojara cierre del mes anterior
        #     currentMonth = date.today()                         #Toma la fecha actual
        #     currentMonth.replace(day = 1)                       #Transforma al primer dia del mes actual
        #     wrongEndDate = currentMonth - timedelta(days = 1)        #Transforma al ultimo dia del mes anterior
        #     endDate = wrongEndDate.strftime("%Y%m%d")             #Formatea fecha de fin
        
        # elif day_str == 'Friday':       #Si es viernes; arrojara lo que lleva del mes actual
        endDate = date.today().strftime("%Y%m%d")       #Entrega del ultima dia del mes actual formateado

        text = ConverText.converTextFormatSQL('LVPinventory.sql',self.codeHouse, self.wareHouse, self.schemeDB, endDate)
        data , description = extracData(text)
        ConverText.ConverDataXlsx(description, data, self.nameInventory)
        print(self.nameInventory)

    