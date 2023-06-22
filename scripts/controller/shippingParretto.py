from components  import sendMail
from components.sendMail import sendMailEcxel
from generator.parrettoGeneration import ParrettoSend
from components.transformData import exportHTML, dateNowHana, dateNowFormat
import json
import os

def sendParrettoCurrent():
    """ Modulo Encargado de Gestionar la lectura del Json Junto con el Envio de los archivos Generados """

    dataJSON = open(os.path.join(os.path.dirname(os.path.abspath('config')),'scripts/config/data.json'), "r")
    dataJSON = json.loads(str(dataJSON.read()))
    #Contron de Lectura
    for i in dataJSON:
        print(i)
        triggerData = ParrettoSend (   
            schemeDB= dataJSON[i]['ShemeDB'],
            wareHouse= dataJSON[i]['codeCellers'],
            codeHouse= dataJSON[i]['codeHouse'],
            nameHouse= dataJSON[i]['nameHouse'])
        triggerMail = sendMailEcxel(
            dataJSON[i]['sender'],
            dataJSON[i]['addresse'],
            "Sabana de Ventas para Liquidaciones".format(dataJSON[i]['nameHouse'],dateNowFormat()),
            exportHTML('massiveParretto.html', date_today = dateNowFormat(), 
                       distributor_entity = dataJSON[i]['nameHouse']),
            triggerData.nameArchivo()
            )
        triggerData.transformData()
        print('Se Genero: ', triggerData.nameHouse)
        triggerMail.sendProviderEmail()
        
