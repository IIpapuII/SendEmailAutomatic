from components.transformData import fromListToString
from components.sendMail import sendMailEcxel
from generator.IrInventoryReportGeneration import InventoryReportSend
from components.transformData import exportHTML, dateNowFormat
from components.dataExtract import extracJSON
from datetime import datetime

def sendInventoryReport(): 
    """ Modulo Encargado de Gestionar la lectura del Json Junto con el Envio de los archivos Generados """
    dateTodayNumber = datetime.now().day

    if dateTodayNumber == 1 or dateTodayNumber == 15:

        dataJSON = extracJSON('supplier.json')
        dateToday = dateNowFormat()
        
        for wayDB in range(2):  #Seleccionamos base de datos
            
            masterKey, DBKey, storePlaceCod, storePlaceName = InventoryReportSend.processingData(dataJSON, wayDB) #Seleccionamos bodega
            i = 0

            for supplierKey in masterKey:

                supplierMasterData = dataJSON[supplierKey]
                storePlaceCodSelected = storePlaceCod[i]
                storePlaceNameSelected = storePlaceName[i]
                    
                for supplier, data in supplierMasterData.items(): #Seleccionar proveedor e información
                    codSupRef = fromListToString(str(data[0]))
                    nameSupRef = fromListToString(str(data[1]))

                    triggerData = InventoryReportSend (schemeDB= dataJSON[DBKey]['schemeDB'], 
                                                    codeStore= storePlaceCodSelected, 
                                                    nameStore= storePlaceNameSelected,
                                                    codeSupplier= codSupRef,
                                                    nameSupplier= nameSupRef)
                    triggerData.transformDataSupplier()

                    if triggerData.transformDataSupplier() == "Stop":
                        print(fromListToString(str(data[1])), 'No tiene productos en bodega con mas de 60 dias')
                    else:
                        triggerMail = sendMailEcxel(
                        dataJSON[DBKey]['sender'],
                        str(data[2]),
                        "Apoyo comercial a productos de baja rotación",
                        exportHTML('InventoryReport.html',
                                    date_now = dateToday,
                                    date_days = dateTodayNumber,
                                    supplier = fromListToString(str(data[1]))),
                        'Productos de ' + nameSupRef + ' con mas de 60 dias en bodega ' + storePlaceNameSelected + '.xlsx',
                        dataJSON[DBKey]['password']
                        )
                        print('Se Genero: ', str(data[1]))
                        triggerMail.sendProviderEmail()
                
                i += 1
    
    else: 
        print("Los correos se enviaran unicamente los 1 y 15 de cada mes")