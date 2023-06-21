from components  import sendMail
from components.sendMail import sendMailEcxel
from generator.dataGeneration import ProveedoresSend
from components.transformData import exportHTML, dateNowHana, dateNowFormat
import json
import os

def sendInventorySupplier():
    """ Modulo Encargado de Gestionar la lectura del Json Junto con el Envio de los archivos Generados """

    dataJSON = open(os.path.join(os.path.dirname(os.path.abspath('config')),'SendEmailAutomatic/scripts/config/data.json'), "r")
    dataJSON = json.loads(str(dataJSON.read()))
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
            triggerData.nameArchivo()
            )
        triggerData.transformData()
        print('Se Genero: ', triggerData.nameHouse)
        triggerMail.sendProviderEmail()
        
