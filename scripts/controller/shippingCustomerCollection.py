from components.sendMail import sendMailEcxel
from generator.customerCollectionGeneration import CustomerCollectionSend
from components.transformData import exportHTML, dateNowFormat,convertNumberToText,formatNumberMoney
import json
import os
import jinja2

def sendCustomerCollectionMail():
    """ Modulo Encargado de Gestionar la lectura del Json Junto con el Envio de los archivos Generados """

    dataJSON = open(os.path.join(os.path.dirname(os.path.abspath('config')),'scripts/config/client.json'), "r")
    dataJSON = json.loads(str(dataJSON.read()))

    #Control de Lectura
    for i in dataJSON:
        print(i)
        container = CustomerCollectionSend(schemeDB= dataJSON[i]['ShemeDB'],
            codeHouse= dataJSON[i]['codeHouse'],
            nameHouse= dataJSON[i]['nameHouse'])
        nameClient, ccCLient, endDateCheck, wait, coin, email  = container.transformData()
        coin_format, coin_ref = formatNumberMoney(coin)
        

        triggerMail = sendMailEcxel(
            dataJSON[i]['sender'], 
            email,
            "Notificación de Cobro".format(dataJSON[i]['nameHouse'],dateNowFormat()),
            exportHTML('customerCollection.html', date_today = dateNowFormat(), 
                       client_name = nameClient, 
                       client_cc = ccCLient, 
                       date_late_payment = endDateCheck,
                       date_waiting = wait,
                       money_number = coin_format,
                       money_letter = convertNumberToText(coin),
                       money_ref = coin_ref,
                       distributor_entity =(dataJSON[i]['nameHouse'])), None)
        
        triggerMail.sendProviderEmail()