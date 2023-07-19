from components.sendMail import sendMailEcxel
from generator.IrInventoryReportGeneration import InventoryReportSend
from components.transformData import exportHTML, dateNowFormat
from components.dataExtract import extracJSON
from datetime import datetime



def sendParrettoCurrent(): 
    """ Modulo Encargado de Gestionar la lectura del Json Junto con el Envio de los archivos Generados """

    dataJSON = extracJSON('supplier.json')
    date_today = dateNowFormat()

    for i in dataJSON:  # Seleccionamos base de datos
        print(i)    
        key = 

        if key:

            for supplier, data in dataJSON.items[key]: #Seleccionamos proveedor
                triggerData = InventoryReportSend (schemeDB= dataJSON[i]['schemeDB'], ref_supplier= supplier)
                triggerMail = sendMailEcxel(
                dataJSON[i]['sender'],
                dataJSON[i]['addresse'],
                "Apoyo comercial a productos de baja rotación",
                exportHTML('InventoryReport.html',
                            date_now = date_today,
                            date_days = datetime.now().day,
                            distributor_entity = dataJSON[i]['nameHouse']),
                'Parretto de Ventas.xlsx',
                dataJSON[i]['password']
                )
                triggerData.transformData()
                print('Se Genero:', supplier)
                triggerMail.sendProviderEmail()

            if j == "Proveedores_Ocaña":
                    break
        
        if i == "Bodega_Gran Distribuidor":
            break

        
