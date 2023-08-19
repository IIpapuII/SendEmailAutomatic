from components.converTextData import ConverText
from components.dataExtract import extracData


class KccParrettoGelvezDistSend():
    """
    Generador de Archivos multiples para proveedor especifico Caso 1
    """

    def __init__(self, GLschemeDB, GLwareHouse, GLsupplierHouse, GLnameDocument):
        self.GLschemeDB = GLschemeDB
        self.GLwareHouse = GLwareHouse
        self.GLsupplierHouse = GLsupplierHouse
        self.GLnameDocument = GLnameDocument
   
    def transformGelvez(self):
        text = ConverText.converTextFormatSQL('KccParrettoVentas.sql', self.GLschemeDB, self.GLwareHouse, self.GLsupplierHouse)
        datas, nameRows = extracData(text)
        ConverText.ConverDataXlsx(nameRows,datas,self.GLnameDocument)
        print("Elemento Guardado.")

class KccParrettoGranDistSend():
    """
    Generador de Archivos multiples para proveedor especifico Caso 1
    """

    def __init__(self, GRschemeDB, GRwareHouse, GRsupplierHouse, GRnameDocument):
        self.GRschemeDB = GRschemeDB
        self.GRwareHouse = GRwareHouse
        self.GRsupplierHouse = GRsupplierHouse
        self.GRnameDocument = GRnameDocument
    
    def transformGran(self):
        text = ConverText.converTextFormatSQL('KccParrettoVentas.sql', self.GRschemeDB, self.GRwareHouse, self.GRsupplierHouse)
        datas, nameRows = extracData(text)
        ConverText.ConverDataXlsx(nameRows,datas,self.GRnameDocument)
        print("Elemento Guardado.")