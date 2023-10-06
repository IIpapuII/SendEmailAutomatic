from components.sendMail import sendMailEcxel
from generator.SpecificParretoGeneration import SpecificParretoSend
from components.transformData import exportHTML, dateNowFormat
from components.dataExtract import extracJSON


def sendSpecificParreto():
    """ Modulo encargado de gestionar la lectura del JSON junto con el envio del archivo generado """

    #Extrae informacion del JSON
    dataJSON = extracJSON('specificparreto.json')

    for i in dataJSON:
        print(i)
        
        #Estancia variables para generacion de archivo
        triggerDOC = SpecificParretoSend( 
            schemeDB= dataJSON[i]['schemeDB'],
            wareHouse= dataJSON[i]['wareHouse'],
            supplierHouse= dataJSON[i]['supplierHouse'],
            nameDocument= dataJSON[i]['nameDocument']
        )
        #Estancia variables para envio de correo
        triggerMail = sendMailEcxel(
            dataJSON[i]['sender'],
            dataJSON[i]['addresse'], 
            "Sabana de Ventas " + dateNowFormat(),
            exportHTML('SpecificParreto.html', date_today = dateNowFormat(), 
                       distributor_entity = dataJSON[i]['nameHouse'],
                       name = i),
            dataJSON[i]['nameDocument'],
            dataJSON[i]['password']
            )
        triggerDOC.transformData()  #Ejecucion de modulo encargado de generar archivo
        print('Se Genero: Archivo -', dataJSON[i]['nameDocument'])
        triggerMail.sendProviderEmail() #Ejecucion de modulo encargado de enviar correo