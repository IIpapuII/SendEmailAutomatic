from components.converTextData import ConverText
from components.dataExtract import extracData

"""
Generador de Archivo CUCUTA para KIMBERLY 
"""
class KccParrettoGelvezDistSend():

    def __init__(self, GLschemeDB, GLwareHouse, GLsupplierHouse):
        self.GLschemeDB = GLschemeDB
        self.GLwareHouse = GLwareHouse
        self.GLsupplierHouse = GLsupplierHouse
   
    def transformGelvez(self):
        text = ConverText.converTextFormatSQL('KccParrettoVentas.sql', self.GLschemeDB, self.GLwareHouse, self.GLsupplierHouse)
        datas, nameRows = extracData(text)
        ConverText.ConverDataXlsx(nameRows,datas,'Sabana de Ventas Kimberly - Gelvez Distribuciones.xlsx')
        print("Elemento Guardado.")

"""
Generador de Archivo CUCUTA para KIMBERLY 
"""
class KccParrettoGranDistSend():

    def __init__(self, GRschemeDB, GRwareHouse, GRsupplierHouse):
        self.GRschemeDB = GRschemeDB
        self.GRwareHouse = GRwareHouse
        self.GRsupplierHouse = GRsupplierHouse
    
    def transformGran(self):
        text = ConverText.converTextFormatSQL('KccParrettoVentas.sql', self.GRschemeDB, self.GRwareHouse, self.GRsupplierHouse)
        datas, nameRows = extracData(text)
        ConverText.ConverDataXlsx(nameRows,datas,'Sabana de Ventas Kimberly - Gran Distribuidor.xlsx')
        print("Elemento Guardado.")