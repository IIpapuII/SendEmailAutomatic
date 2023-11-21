from components.sendMail import sendMailEcxel
from generator.parrettoCLGTgeneration import CLGTparrettoGLVsend
from components.transformData import exportHTML, dateNowFormat
from components.dataExtract import extracJSON


def sendCLGTparretto():
    """ Modulo Encargado de Gestionar la lectura del Json Junto con el Envio de los archivos Generados """

    dataJSON = extracJSON('CLGTparretto.json')              #Lectura de Json

    for i in dataJSON:
        print(i)
        
        if i == "EMAIL":                        #Establece variables para envio de correo
            sender= dataJSON[i]['sender']
            password= dataJSON[i]['password']
            nameHouse= dataJSON[i]['nameHouse']
            addresse= dataJSON[i]['addresse']
        elif str(i).count('Z') > 0:
            triggerGelvez = CLGTparrettoGLVsend(                #Establece variables para creacion de sabana de ventas
                GLschemeDB= dataJSON[i]['GLschemeDB'],
                GLwareHouse= dataJSON[i]['GLwareHouse'],
                GLsupplierHouse= dataJSON[i]['GLsupplierHouse'],
                GLnameDocument= dataJSON[i]['GLnameDocument']
                )
            gelvez = i
    
    triggerMail = sendMailEcxel(                #Adjunta informes y prepara correo
        sender,
        addresse,
        "Sabana de Ventas - Colgate",
        exportHTML('CLGTmessage.html', date_today = dateNowFormat, distributor_entity = nameHouse),
        dataJSON[gelvez]['GLnameDocument'],
        password
        )
    triggerGelvez.transformGelvez()                 #Ejecuta creacion de sabana de ventas
    print('Se Genero: Archivo Colgate ', gelvez)
    triggerMail.sendProviderEmail()                 #Envia correo