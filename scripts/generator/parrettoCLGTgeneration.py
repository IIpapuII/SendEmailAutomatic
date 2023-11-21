from components.converTextData import ConverText
from components.dataExtract import extracData


class CLGTparrettoGLVsend():
    """ Modulo encargado de la generacion de archivos en base a variable establecidas"""
    def __init__(self, GLschemeDB, GLwareHouse, GLsupplierHouse, GLnameDocument):
        self.GLschemeDB = GLschemeDB
        self.GLwareHouse = GLwareHouse
        self.GLsupplierHouse = GLsupplierHouse
        self.GLnameDocument = GLnameDocument
   
    def transformGelvez(self):
        #Procesa informacion de una consulta SQL y la transforma a Excel
        text = ConverText.converTextFormatSQL('CLGTparretto.sql', self.GLschemeDB, self.GLwareHouse, self.GLsupplierHouse)
        datas, nameRows = extracData(text)
        ConverText.ConverDataXlsx(nameRows,datas,self.GLnameDocument)
        print("Elemento Guardado.")