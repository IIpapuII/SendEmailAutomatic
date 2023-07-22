from components.transformData import fromListToString
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
    def __init__(self, schemeDB, codeStore, codeSupplier, nameSupplier, nameStore):
        self.schemeDB = schemeDB
        self.codeStore = codeStore
        self.nameStore = nameStore
        self.codeSupplier = codeSupplier
        self.nameSupplier = nameSupplier
    
    def transformDataSupplier(self):
        text = ConverText.converTextFormatSQL('IrInventoryReport.sql', self.schemeDB, self.codeStore, self.codeSupplier )
        datas, nameRows = extracData(text)
        listRef = []
        Stop = "Stop"
        
        for ref in datas:
            listRef.append(ref)

        if listRef == []:
            return Stop
        else:
            ConverText.ConverDataXlsx(nameRows, datas, 'Productos de ' + self.nameSupplier + ' con mas de 60 dias en bodega ' + self.nameStore + '.xlsx')
            print("Elemento Guardado.")
    
    def transformDataSupervisor(self):
        text = ConverText.converTextFormatSQL('IrInventoryReport.sql', self.schemeDB, self.codeStore, self.codeSupplier )
        datas, nameRows = extracData(text)
        listRef = []
        Stop = "Stop"
        
        for ref in datas:
            listRef.append(ref)

        if listRef == []:
            return Stop
        else:
            ConverText.ConverDataXlsx(nameRows, datas, 'Productos de ' + self.nameSupplier + ' con mas de 60 dias en bodega ' + self.nameStore + '.xlsx')
            print("Elemento Guardado.")

    def processingData(dataJSON: dict, way: int):
        listKey = []
        i = 0
        storePlaceCod = []
        storePlaceName = []

        for key in dataJSON:
            listKey.append(key)

        if way == 0: 
            DBKey = fromListToString(str(listKey[0]))  # Selecciona Grupo de Bodega
            masterKey = [listKey[2], listKey[3]]
        elif way == 1:
            DBKey = fromListToString(str(listKey[1]))
            masterKey = [listKey[4], listKey[5], listKey[6]]

        schemeConformedElements = dataJSON[listKey[way]]

        for title, data in schemeConformedElements.items(): #Selecciona codigo de bodega y nombre
            if i < 4:
                i += 1
            if  i >= 4:
                storePlaceCod.append(data)
                storePlaceName.append(title)
        
        return masterKey, DBKey, storePlaceCod, storePlaceName
            