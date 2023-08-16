from components.sendMail import sendMailEcxel
from generator.IrInventoryReportGeneration import InventoryReportSend
from components.transformData import exportHTML, dateNowPC
from components.dataExtract import extracJSON
from datetime import datetime

def sendInventoryReport(): 
    """ Modulo Encargado de Gestionar la lectura del Json Junto con el Envio de los archivos Generados """
    dateTodayNumber = datetime.now().day

    if dateTodayNumber == 1 or dateTodayNumber == 15:  #Solo se puede enviar este correo el 1ro y 15vo dia de un mes

        if dateTodayNumber == 1:
            dataJSON = extracJSON('suppliers.json') #Si es 1ro, se escojera json de proveedores
        elif dateTodayNumber == 15:
            dataJSON = extracJSON('supervisors.json')   #Si es 15vo, se escojera json de supervisores

        dateToday = dateNowPC()
        
        for origin in dataJSON:  #Seleccionamos proveedor/supervisor
            listDefinition = []
            listWord = []
            title = dataJSON[origin]
            i = 0

            for word, definition in title.items():
                listWord.append(word)
                listDefinition.append(definition)

            listWord = listWord[2:]
            listDefinition = listDefinition[2:]
            
            for ref in listDefinition:
                triggerData = InventoryReportSend (schemeDB= ref[2],
                                                    codeStore= ref[1],
                                                    nameStore= listWord[i],
                                                    codeSupplier= ref[0],
                                                    header= origin,
                                                    date= dateTodayNumber)
                triggerData.transformDataSS() 

                if triggerData.transformDataSS() == "Stop":
                    print(origin, ' - No tiene productos en bodega con mas de 60 dias')
                else:
                    triggerMail = sendMailEcxel(
                    title['sender'],
                    ref[3],
                    "Apoyo comercial a productos de baja rotación",
                    exportHTML('InventoryReport.html',
                                date_now = dateToday,
                                date_days = dateTodayNumber,
                                supplier = origin,
                                store = listWord[i],
                                depot = origin),
                    'Productos con mas de 60 dias en bodega ' + listWord[i] + ' ' + origin + '.xlsx',
                    title['password']
                    )
                    print('Se Genero: ', origin, " - ", listWord[i])
                    triggerMail.sendProviderEmail()
                i += 1
    else: 
        print("Los correos se enviaran unicamente los 1 y 15 de cada mes")