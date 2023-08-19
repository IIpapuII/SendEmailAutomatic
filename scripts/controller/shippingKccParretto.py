from components.sendMail import sendMailEcxelMultiple
from generator.KccParrettoGeneration import KccParrettoGranDistSend, KccParrettoGelvezDistSend
from components.transformData import exportHTML, dateNowFormat
from components.dataExtract import extracJSON


def sendKccParretto():
    """ Modulo Encargado de Gestionar la lectura del Json Junto con el Envio de los archivos Generados """

    dataJSON = extracJSON('kccparreto.json')


    for i in dataJSON:
        print(i)
        
        if i == "EMAIL":
            sender= dataJSON[i]['sender']
            password= dataJSON[i]['password']
            nameHouse= dataJSON[i]['nameHouse']
            addresse= dataJSON[i]['addresse']
        elif str(i).count('Z') > 0:
            triggerGelvez = KccParrettoGelvezDistSend(   
                GLschemeDB= dataJSON[i]['GLschemeDB'],
                GLwareHouse= dataJSON[i]['GLwareHouse'],
                GLsupplierHouse= dataJSON[i]['GLsupplierHouse']
                )
            gelvez = i
        else:
            triggerGran = KccParrettoGranDistSend(   
                GRschemeDB= dataJSON[i]['GRschemeDB'],
                GRwareHouse= dataJSON[i]['GRwareHouse'],
                GRsupplierHouse= dataJSON[i]['GRsupplierHouse']
                )
            gran = i
        triggerMail = sendMailEcxelMultiple(
            sender,
            addresse,
            "Sabana de Ventas - Kimberly",
            exportHTML('kccParretto.html', date_today = dateNowFormat, distributor_entity = nameHouse),
            ['Sabana de Ventas Kimberly - Gelvez Distribuciones.xlsx','Sabana de Ventas Kimberly - Gran Distribuidor.xlsx'],
            password
            )
    triggerGelvez.transformGelvez()
    triggerGran.transformGran()
    print('Se Genero: Archivo Kimberly ', gelvez," - ",gran)
    triggerMail.sendProviderEmail()