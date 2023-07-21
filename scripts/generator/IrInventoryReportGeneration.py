from model.conectDB import conect
from components.converTextData import ConverText
from components.dataExtract import extracData
from components.sendMail import sendMailEcxel


"""
Modulo Encardo de la conexión a la base y generación del archivo de ecxel 
"""
coon = conect()
class InventoryReportSend():
    """
    Se encarga de generar el proceso de envio de la sabana de ventas para el proceso de 
    solicitudes de invercción 
    """
    def __init__(self, schemeDB, codeStore, codeSupplier):
        self.schemeDB = schemeDB
        self.codeStore = codeStore
        self.codeSupplier = codeSupplier
        
    
    def transformData(self):
        text = ConverText.converTextFormatSQL('IrInventoryReport.sql', self.schemeDB, 
                                              self.codeStore, self.codeSupplier)
        datas, nameRows = extracData(text)
        ConverText.ConverDataXlsx(nameRows,datas,'Productos con mas de 60 dias en bodega.xlsx')
        print("Elemento Guardado.")

    def processingData(self, dataJSON, way):
        listKey = []
        i = 0
        storePlace = []

        for key in dataJSON:
            listKey.append(key)

        if way == 0: 
            DBKey = str(listKey[0]).replace("[","").replace("]","")
            masterKey = [listKey[2], listKey[3]]
        elif way == 1:
            DBKey = str(listKey[1]).replace("[","").replace("]","")
            masterKey = [listKey[4], listKey[5], listKey[6]]

        schemeConformedElements = dataJSON[listKey[way]]

        for title, data in schemeConformedElements.items():
            if i < 4:
                i += 1
            if  i >= 4:
                storePlace.append(data)
        
        return masterKey, DBKey, storePlace
            