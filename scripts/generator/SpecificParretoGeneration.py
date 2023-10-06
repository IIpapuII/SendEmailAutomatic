from components.converTextData import ConverText
from components.dataExtract import extracData


class SpecificParretoSend():
    """
    Modulo que genera y guarda sabana de ventas especifica
    """

    #Estableciendo variables generales de clase
    def __init__(self, schemeDB, wareHouse, supplierHouse, nameDocument):
        self.schemeDB = schemeDB
        self.wareHouse = wareHouse
        self.supplierHouse = supplierHouse
        self.nameDocument = nameDocument
    
    #Generacion y guardado de archivo
    def transformData(self):
        text = ConverText.converTextFormatSQL('SpecificParreto.sql', self.schemeDB, self.wareHouse, self.supplierHouse)
        datas, nameRows = extracData(text)
        ConverText.ConverDataXlsx(nameRows,datas,self.nameDocument)
        print("Elemento Guardado.")