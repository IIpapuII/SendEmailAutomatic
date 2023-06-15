from components  import sendMail
from components.sendMail import sendMailEcxel
from generator.dataGeneration import ProveedoresSend
from components.transformData import exportHTML, dateNowHana
import json
import os

def sendInventorySupplier():
    """ Modulo Encargado de Gestionar la lectura del Json Junto con el Envio de los archivos Generados """

    dataJSON = open(os.path.join(os.path.dirname(os.path.abspath('config')),'scripts/config/data.json'), "r")
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
            dataJSON[i]['nameHouse'],
            exportHTML('menssage.html', NameHouse = dataJSON[i]['nameHouse'], 
                       listWhareHouse = dataJSON[i]['nameCellers']),
            triggerData.nameArchivo()
            )
        triggerData.transformData()
        print('Se Genero: ', triggerData.nameHouse)
        triggerMail.sendProviderEmail()
        
