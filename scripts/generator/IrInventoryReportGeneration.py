from model.conectDB import conect
from components.converTextData import ConverText
from components.dataExtract import extracData
from datetime import datetime

"""
Modulo Encardo de la conexión a la base y generación del archivo de ecxel 
"""
coon = conect()
class InventoryReportSend():
    """
    Se encarga de generar el proceso de envio de la sabana de ventas para el proceso de 
    solicitudes de invercción 
    """
    def __init__(self, schemeDB, codeStore, nameStore, codeSupplier, header, date):
        self.schemeDB = schemeDB
        self.codeStore = codeStore
        self.nameStore = nameStore
        self.codeSupplier = codeSupplier
        self.header = header
        self.date = date
    
    def transformDataSS(self):

        text = ConverText.converTextFormatSQL('IrInventoryReport.sql', self.schemeDB, self.codeStore, self.codeSupplier )
        datas, nameRows = extracData(text)
        listRef = []
        Stop = "Stop"
        
        for ref in datas:
            listRef.append(ref)

        if listRef == []:
            return Stop
        else:
            ConverText.ConverDataXlsx(nameRows, datas, 'Productos con mas de 60 dias en bodega ' + self.nameStore + ' ' + self.header + '.xlsx')
            print("Elemento Guardado.")