from components  import sendMail
from components.sendMail import sendMailEcxel
from generator.dataGeneration import ProveedoresSend
from components.transformData import exportHTML, dateNowHana, dateNowFormat
from components.dataExtract import extracJSON
import json
import os

def sendInventorySupplier():
    """ Modulo Encargado de Gestionar la lectura del Json Junto con el Envio de los archivos Generados """

    dataJSON = extracJSON('data.json')
    #Contron de Lectura
    for i in dataJSON:
        print(i)
        triggerData = ProveedoresSend(   
            schemeDB= dataJSON[i]['ShemeDB'],
            wareHouse= dataJSON[i]['codeCellers'],
            codeHouse= dataJSON[i]['codeHouse'],
            nameHouse= dataJSON[i]['nameHouse'])
        triggerMail = sendMailEcxel(
            dataJSON[i]['sender'],
            dataJSON[i]['addresse'],
            "Inventario de {0} a corte de {1}".format(dataJSON[i]['nameHouse'],dateNowFormat()),
            exportHTML('menssage.html', NameHouse = dataJSON[i]['nameHouse'], 
                       listWhareHouse = dataJSON[i]['nameCellers']),
            triggerData.nameArchivo(),
            dataJSON[i]['password']
            )
        triggerData.transformData()
        print('Se Genero: ', triggerData.nameHouse)
        triggerMail.sendProviderEmail()
        
