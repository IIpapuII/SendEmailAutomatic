from model.modelSQL import Structure
from components.converTextData import ConverText
from components.dataExtract import extracData

class parretoLVPsend(Structure):
    """ Modulo encargado de la generacion de archivos en base a variable establecidas"""
    def __init__(self, schemeDB, 
                 wareHouse, nameParreto,
                 initDate=None, 
                 endDate=None,
                 wareCellers = None ) -> None:
        super().__init__(schemeDB, wareHouse, initDate, endDate)
        self.wareCellers = wareCellers
        self.nameParreto = nameParreto
    
    def Controlle(self):
        #Procesa informacion de una consulta SQL y la transforma a Excel
        text = ConverText.converTextFormatSQL('LVPparreto.sql', self.schemeDB, self.wareHouse, self.initDate, self.endDate, self.wareCellers)
        data , description = extracData(text)
        ConverText.ConverDataXlsx(description, data, self.nameParreto)
        print(self.nameParreto)


