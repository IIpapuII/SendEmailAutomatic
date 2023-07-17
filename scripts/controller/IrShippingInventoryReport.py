from components.sendMail import sendMailEcxel
from generator.IrInventoryReportGeneration import InventoryReportSend
from components.transformData import exportHTML, dateNowFormat
from components.dataExtract import extracJSON



def sendParrettoCurrent():
    """ Modulo Encargado de Gestionar la lectura del Json Junto con el Envio de los archivos Generados """

    dataJSON = extracJSON('supplier.json')

    for i in dataJSON:  # Seleccionamos base de datos
        print(i)  
        foundedGelvez = False
        foundedGran = False

        if i == "BD_Gelvez": #Seleccionamos BD

            for j in dataJSON:  

                if j == "Proveedores_Cucuta": #Seleccionamos bodega
                    foundedGelvez = True

                if foundedGelvez:

                    for supplier, data in dataJSON.items[j]: #Seleccionamos proveedor
                        triggerData = InventoryReportSend (schemeDB= dataJSON[i]['schemeDB'], ref_supplier= supplier)
                        triggerMail = sendMailEcxel(
                            dataJSON[i]['sender'],
                            dataJSON[i]['addresse'],
                            "Apoyo comercial a productos de baja rotación",
                            exportHTML('InventoryReport.html', date_today = dateNowFormat(), distributor_entity = dataJSON[i]['nameHouse']),
                            'Parretto de Ventas.xlsx',
                            dataJSON[i]['password']
                            )
                        triggerData.transformData()
                        print('Se Genero:', supplier)
                        triggerMail.sendProviderEmail()

                if j == "Proveedores_Ocaña":
                    break
        
        if i == "BD_Gran Distribuidor": #Seleccionamos BD

            for j in dataJSON:

                if j == "Proveedores_Giron": #Seleccionamos bodega
                    foundedGran = True

                if foundedGran:

                    for supplier, data in dataJSON.keys[j]: #Seleccionamos proveedor
                        triggerData = InventoryReportSend (schemeDB= dataJSON[i]['schemeDB'], ref_supplier= supplier)
                        
                        triggerMail = sendMailEcxel(
                            dataJSON[i]['sender'],
                            dataJSON[i]['addresse'],
                            "Sabana de Ventas para Liquidaciones," + dateNowFormat(),
                            exportHTML('massiveParretto.html', date_today = dateNowFormat(), distributor_entity = dataJSON[i]['nameHouse']),
                            'Parretto de Ventas.xlsx',
                            dataJSON[i]['password']
                            )
                        triggerData.transformData()
                        print('Se Genero: Sabana de ventas')
                        triggerMail.sendProviderEmail()      

                if j == "Proveedores_Eje":
                    break  

        if i == "Bodega_Gran Distribuidor":
            break

        
