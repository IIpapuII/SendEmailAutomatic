from components.sendMail import sendMailEcxelMultiple
from generator.inventoryLVPgeneration import inventoryLVPsend
from generator.parretoLVPgeneration import parretoLVPsend
from components.transformData import exportHTML, dateNowHana, dateNowFormat, dateFirstDay
from components.dataExtract import extracJSON
from components.dataExtract import getFilePath
import pandas as pd


def sendLVPreport():
    """ Modulo Encargado de Gestionar la lectura del Json Junto con el Envio de los archivos Generados """

    dataJSON = extracJSON('LVPdata.json')           #Lectura de Json

    for i in dataJSON:
        print(i)
        triggerData = inventoryLVPsend(         #Establece variables para creacion de inventario
            schemeDB= dataJSON[i]['ShemeDB'],
            wareHouse= dataJSON[i]['codeCellers'],
            codeHouse= dataJSON[i]['codeHouse'],
            nameHouse= dataJSON[i]['nameHouse'],
            nameInventory = dataJSON[i]['nameInventory']
        )
        triggerSales = parretoLVPsend(              #Establece variables para creacion de sabana de ventas
            schemeDB= dataJSON[i]['ShemeDB'],
            wareHouse= dataJSON[i]['codeHouse'],
            initDate= dateFirstDay(),
            endDate= dateNowHana(),
            wareCellers= dataJSON[i]['codeCellers'],
            nameParreto = dataJSON[i]['nameParreto']
        )
        triggerData.transformData()             #Ejecuta creacion de inventario
        triggerSales.Controlle()          #Ejecuta creacion de sabana de ventas

    salesSheet = [getFilePath('docs',dataJSON['LVP GEL']['nameParreto']), getFilePath('docs',dataJSON['LVP GRA']['nameParreto'])]
    Inventory = [getFilePath('docs',dataJSON['LVP GEL']['nameInventory']), getFilePath('docs',dataJSON['LVP GRA']['nameInventory'])]
    read_salesSheet = [pd.read_excel(i) for i in salesSheet]
    read_Inventory = [pd.read_excel(i) for i in Inventory]
    result_salesSheet = pd.concat(read_salesSheet, ignore_index= True)                  #Unifica informes
    result_Inventory = pd.concat(read_Inventory, ignore_index= True)
    result_salesSheet.to_excel(getFilePath('docs','Sabana de Ventas - {0}.xlsx'.format(dataJSON[i]['nameHouse'])))
    result_Inventory.to_excel(getFilePath('docs','Inventario - {0}.xlsx'.format(dataJSON[i]['nameHouse'])))

    triggerMail = sendMailEcxelMultiple(                    #Adjunta informes y prepara correo
        dataJSON[i]['sender'],
        dataJSON[i]['addresse'],
        "Inventario y Ventas de {0} a corte de {1}".format(dataJSON[i]['nameHouse'],dateNowFormat()),
        exportHTML('LVPreport.html', NameHouse = dataJSON[i]['nameHouse'],
                    listWhareHouse = dataJSON[i]['nameCellers']),
        ['Sabana de Ventas - {0}.xlsx'.format(dataJSON[i]['nameHouse']), 'Inventario - {0}.xlsx'.format(dataJSON[i]['nameHouse'])],
        dataJSON[i]['password']
    )
    print('Se Genero: ', triggerData.nameHouse)
    triggerMail.sendProviderEmail() #Envia correo