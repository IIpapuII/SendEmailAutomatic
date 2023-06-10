from components.sendMail import sendMailEcxel
from generator.icomeGenerateDate import SendIcomes
from components.dataExtract import extracJSON
from components.transformData import dateNowHana

def sendIcomesJson():
    
    dataJSON = extracJSON('icomessend.json')

    for i in dataJSON:
        triggerData = SendIcomes(
            dataJSON[i]['schemeDB'],
            dataJSON[i]['wareHouse'],
            '20230601',
            '20230610'
        )
        triggerMail = sendMailEcxel(
            dataJSON[i]['sender'],
            dataJSON[i]['addresse'],
            'Entrada de Mercancia',
            'Mensaje de prueba',
            'IngresoMercancia.xlsx'
        )
        if triggerData.controllerIcome() == False:
            print('No Se envia ')
        else:
            triggerMail.sendProviderEmail()
        

    

    
