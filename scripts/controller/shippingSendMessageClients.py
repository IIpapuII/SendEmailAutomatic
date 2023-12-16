from components.sendMail import sendMailEcxel
from generator.sendMessageClientsGeneration import SendMessageClients
from components.dataExtract import extracJSON
from components.transformData import exportHTML
import pandas as pd
import os
from components.sendMail import sendMailEcxel

def sendMessageClients():
    """ Modulo encargado de gestionar la lectura del ".json" junto con el envio de correo con mensaje especifico """
    
    dataJSON = extracJSON('message.json')

    print("Ingrese que Excel a buscar:")
    print("Gran Dist. = 1 / Gelvez Dist. = 0")
    key = input(">")

    if key == '0' or key == '1':
        #Control de Lectura
        registers = []

        if key == '0':
            df = pd.read_excel(os.path.join(os.path.dirname(os.path.abspath('docs')),'scripts/docs/#EnvioMensajesClientes_Gelvez.xlsx'), header=None)
            df_array = df.values

            container = SendMessageClients(schemeDB= dataJSON['message']['ShemeDB_GLVZ'])

            for a in range(len(df_array)):
                space_tempory = df_array[a]
                registers.append(space_tempory[0])

        elif key == '1':
            df = pd.read_excel(os.path.join(os.path.dirname(os.path.abspath('docs')),'scripts/docs/#EnvioMensajesClientes_Gran.xlsx'), header=None)
            df_array = df.values

            container = SendMessageClients(schemeDB= dataJSON['message']['ShemeDB_GRN'])

            for a in range(len(df_array)):
                space_tempory = df_array[a]
                registers.append(space_tempory[0])

        for j in registers:
            print(j)

            cn, name, email  = container.transformData(str(j))

            if email == 'None':
                email = dataJSON['message']['sender']
                        
            triggerMail = sendMailEcxel(
                dataJSON['message']['sender'], 
                email,
                "Beneficios por ProntoPago",                #El asunto de debe ser cambiado dependiendo del
                exportHTML("sendMessageClients.html", date = None), 
                None, 
                dataJSON['message']['password'])

            triggerMail.sendProviderEmail()
            print(cn, " - ", name)

    else:
        print('Ingrese valor correcto por favor')
