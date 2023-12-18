from model.modelSQL import Structure
from components.converTextData import ConverText
from components.dataExtract import extracData
from datetime import date, timedelta
import calendar

class parretoLVPsend(Structure):
    """ Modulo encargado de la generacion de archivos en base a variable establecidas"""
    def __init__(self, schemeDB, 
                 wareHouse, nameParreto,
                 wareCellers = None ) -> None:
        super().__init__(schemeDB, wareHouse)
        self.wareCellers = wareCellers
        self.nameParreto = nameParreto
    
    def Controlle(self):
        #Procesa informacion de una consulta SQL y la transforma a Excel
        day_int = date.today().day
        day_str = calendar.day_name[date.today().weekday()]

        if day_int == 1:        #Si es el primer dia del mes; arrojara cierre del mes anterior
            currentMonth = date.today()                         #Toma la fecha actual
            currentMonth.replace(day = 1)                       #Transforma al primer dia del mes actual
            endDate = currentMonth - timedelta(days = 1)        #Transforma al ultimo dia del mes anterior
            initDate = endDate.replace(day = 1)                 #Transforma al primer dia del mes anterior

            endDate.strftime("%Y%m%d")             #Formatea fecha de fin
            initDate.strftime("%Y%m%d")            #Formatea fecha de inicio
        
        elif day_str == 'Friday':          #Si es viernes; arrojara lo que lleva del mes actual
            endDate = date.today().strftime("%Y%m%d")                       #Entrega del ultima dia del mes actual formateado
            initDate = date.today().replace(day = 1).strftime("%Y%m%d")     #Entrega del primer dia del mes actual formateado

        text = ConverText.converTextFormatSQL('LVPparreto.sql', self.schemeDB, self.wareHouse, initDate, endDate, self.wareCellers)
        data , description = extracData(text)
        ConverText.ConverDataXlsx(description, data, self.nameParreto)
        print(self.nameParreto)


