from components.converTextData import ConverText
from components.dataExtract import extracData


class CLGTparrettoGLVsend():

    def __init__(self, GLschemeDB, GLwareHouse, GLsupplierHouse, GLnameDocument):
        self.GLschemeDB = GLschemeDB
        self.GLwareHouse = GLwareHouse
        self.GLsupplierHouse = GLsupplierHouse
        self.GLnameDocument = GLnameDocument
   
    def transformGelvez(self):
        text = ConverText.converTextFormatSQL('CLGTparretto.sql', self.GLschemeDB, self.GLwareHouse, self.GLsupplierHouse)
        datas, nameRows = extracData(text)
        ConverText.ConverDataXlsx(nameRows,datas,self.GLnameDocument)
        print("Elemento Guardado.")