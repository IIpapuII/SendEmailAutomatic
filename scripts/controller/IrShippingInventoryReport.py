from components.sendMail import sendMailEcxel
from generator.IrInventoryReportGeneration import InventoryReportSend
from components.transformData import exportHTML, dateNowFormat
from components.dataExtract import extracJSON
from datetime import datetime

def sendParrettoCurrent(): 
    """ Modulo Encargado de Gestionar la lectura del Json Junto con el Envio de los archivos Generados """

    dataJSON = extracJSON('supplier.json')
    date_today = dateNowFormat()

    for wayDB in range(2):  #Seleccionamos base de datos
        
        masterKey, DBKey, storePlace = InventoryReportSend.processingData(dataJSON, wayDB) #Seleccionamos bodega
        i = 0

        for supplierKey in masterKey:

            supplierMasterData = dataJSON[supplierKey]
            storePlaceSelected = storePlace[i]
                  
            for supplier, data in supplierMasterData.items(): #Seleccionar proveedor e información
                triggerData = InventoryReportSend (schemeDB= dataJSON[DBKey]['schemeDB'], 
                                                   codeStore= storePlaceSelected, 
                                                   codeSupplier= data[0])
                triggerMail = sendMailEcxel(
                dataJSON[DBKey]['sender'],
                dataJSON[DBKey]['addresse'],
                "Apoyo comercial a productos de baja rotación",
                exportHTML('InventoryReport.html',
                            date_now = date_today,
                            date_days = datetime.now().day,
                            distributor_entity = dataJSON[DBKey]['nameHouse']),
                'Productos con mas de 60 dias en bodega.xlsx',
                dataJSON[DBKey]['password']
                )
                triggerData.transformData()
                print('Se Genero:', supplier)
                triggerMail.sendProviderEmail()
            
            i += 1

            if j == "Proveedores_Ocaña":
                    break
        
        if i == "Bodega_Gran Distribuidor":
            break

        
