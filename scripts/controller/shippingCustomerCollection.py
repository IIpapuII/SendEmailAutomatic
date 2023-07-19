from components.sendMail import sendMailEcxel
from generator.customerCollectionGeneration import CustomerCollectionSend
from components.transformData import exportHTML, dateNowFormat,convertNumberToText,formatNumberMoney
import pandas as pd
import json
import os

def sendCustomerCollectionMail():
    """ Modulo Encargado de Gestionar la lectura del Json Junto con el Envio de los archivos Generados """

    dataJSON = open(os.path.join(os.path.dirname(os.path.abspath('config')),'scripts/config/client.json'), "r")
    dataJSON = json.loads(str(dataJSON.read()))

    key = 0

    #Control de Lectura
    for i in dataJSON:
        print(i)
        container = CustomerCollectionSend(schemeDB= dataJSON[i]['ShemeDB'])

        if key == 0:
            df = pd.read_excel(os.path.join(os.path.dirname(os.path.abspath('docs')),'scripts/docs/ClientesDeudoresGelvez.xlsx'), header=None)
            df_array = df.values
            key += 1
        elif key > 0:
            df = pd.read_excel(os.path.join(os.path.dirname(os.path.abspath('docs')),'scripts/docs/ClientesDeudoresGranDist.xlsx'), header=None)
            df_array = df.values

        for j in range(len(df_array)):
            nameClient, ccCLient, endDateCheck, wait, coin, email  = container.transformData(df_array[j])

            if email == "":
                email = "supporsistemas@c.gelvezdistribuciones.com"
            
            if coin <= 0:
                print("EL cliente no tiene saldo pendiente")
                print(ccCLient, "", nameClient)   
            elif wait < 15:
                print("No llega a 15 dias de mora")
                print(ccCLient, "", nameClient)     
           
            else:
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
                            distributor_entity =(dataJSON[i]['nameHouse'])), 
                    None, 
                    dataJSON[i]['password'])

                triggerMail.sendProviderEmail()