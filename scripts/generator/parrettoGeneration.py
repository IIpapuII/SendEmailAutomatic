from model.conectDB import conect
from components.converTextData import ConverText
from components.dataExtract import extracData

"""
Modulo Encardo de la conexión a la base y generación del archivo de ecxel 
"""
coon = conect()
class ParrettoSend():
    """
    Se encarga de generar el proceso de envio de la sabana de ventas para el proceso de 
    solicitudes de invercción 
    """
    def __init__(self, schemeDB, wareHouse):
        self.schemeDB = schemeDB
        self.wareHouse = wareHouse
    
    
    def transformData(self):
        text = ConverText.converTextFormatSQL('parrettoventas.sql', self.schemeDB, self.wareHouse)
        datas, nameRows = extracData(text)
        ConverText.ConverDataXlsx(nameRows,datas,'Parretto de Ventas.xlsx')
        print("Elemento Guardado.")


    