from components.sendMail import sendMailEcxelMultiple
from generator.inventoryLVPgeneration import inventoryLVPsend
from generator.parretoLVPgeneration import parretoLVPsend
from components.transformData import exportHTML
from components.dataExtract import extracJSON
from components.dataExtract import getFilePath
import pandas as pd
from datetime import date, timedelta
import calendar

def sendLVPreport():
    """ Modulo Encargado de Gestionar la lectura del Json Junto con el Envio de los archivos Generados """

day_int = date.today().day
day_str = calendar.day_name[date.today().weekday()]

if day_int == 1 or day_str == 'Friday':
    dataJSON = extracJSON('LVPdata.json')           #Lectura de Json

    if day_int == 1:        #Si es el primer dia del mes; arrojara cierre del mes anterior
        currentMonth = date.today()                         #Toma la fecha actual
        currentMonth.replace(day = 1)                       #Transforma al primer dia del mes actual
        wrongEndDate = currentMonth - timedelta(days = 1)        #Transforma al ultimo dia del mes anterior
        endDate = wrongEndDate.strftime("%d/%m/%Y")             #Formatea fecha de fin
    
    elif day_str == 'Friday':       #Si es viernes; arrojara lo que lleva del mes actual
        endDate = date.today().strftime("%d/%m/%Y")       #Entrega del ultima dia del mes actual formateado

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
        "Inventario y Ventas de {0} a corte de {1}".format(dataJSON[i]['nameHouse'],endDate),
        exportHTML('LVPreport.html', NameHouse = dataJSON[i]['nameHouse'],
                    listWhareHouse = dataJSON[i]['nameCellers']),
        ['Sabana de Ventas - {0}.xlsx'.format(dataJSON[i]['nameHouse']), 'Inventario - {0}.xlsx'.format(dataJSON[i]['nameHouse'])],
        dataJSON[i]['password']
    )
    print('Se Genero: ', triggerData.nameHouse)
    triggerMail.sendProviderEmail() #Envia correo

else:
    print('Aun no es el tiempo indicado')