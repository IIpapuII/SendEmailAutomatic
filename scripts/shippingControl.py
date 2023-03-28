import sendMail
import dataGeneration
import json
import os

def controlsend():
    """ Modulo Encargado de Gestionar la lectura del Json Junto con el Envio de los archivos Generados """

    dataJSON = open(os.path.join(os.getcwd(),'SendEmailAutomatic/scripts/data.json'), "r")
    dataJSON = json.loads(str(dataJSON.read()))
    #Contron de Lectura
    for i in dataJSON:
        print(i)
        triggerData = dataGeneration.Proveedores(
            dataJSON[i]['codeHouse'],
            dataJSON[i]['nameHouse'],
            dataJSON[i]['codeCellers'],
            dataJSON[i]['ShemeDB'])
        triggerMail = sendMail.sendMail(
            dataJSON[i]['sender'],
            dataJSON[i]['addresse'],
            dataJSON[i]['nameCellers'],
            dataJSON[i]['nameHouse'])
        triggerData.transformData()
        print('Se Genero: ', triggerData.nameHouse)
        triggerMail.sendProviderEmail(triggerData.nameArchivo())
        
