from components  import sendMail
from components.sendMail import sendMailEcxelMultiple
from generator.dataGeneration import ProveedoresSend
from generator.ParretoGenerationSales import ParettoSales
from components.transformData import exportHTML, dateNowHana, dateNowFormat, dateFirstDay
from components.dataExtract import extracJSON


def sendInventorySupplier():
    """ Modulo Encargado de Gestionar la lectura del Json Junto con el Envio de los archivos Generados """

    dataJSON = extracJSON('data.json')
    #Contron de Lectura
    for i in dataJSON:
        print(i)
        triggerData = ProveedoresSend(   
            schemeDB= dataJSON[i]['ShemeDB'],
            wareHouse= dataJSON[i]['codeCellers'],
            codeHouse= dataJSON[i]['codeHouse'],
            nameHouse= dataJSON[i]['nameHouse'])
        triggerSales = ParettoSales(
            schemeDB= dataJSON[i]['ShemeDB'],
            wareHouse= dataJSON[i]['codeHouse'],
            initDate= dateFirstDay(),
            endDate= dateNowHana(),
            wareCellers= dataJSON[i]['codeCellers']

        )
        triggerMail = sendMailEcxelMultiple(
            dataJSON[i]['sender'],
            dataJSON[i]['addresse'],
            "Inventario de {0} a corte de {1}".format(dataJSON[i]['nameHouse'],dateNowFormat()),
            exportHTML('menssage.html', NameHouse = dataJSON[i]['nameHouse'], 
                       listWhareHouse = dataJSON[i]['nameCellers']),
            [triggerData.nameArchivo(),'ArchiveVentas.xlsx'],
            dataJSON[i]['password']
            )
        triggerSales.Controlle()
        triggerData.transformData()
        print('Se Genero: ', triggerData.nameHouse)
        triggerMail.sendProviderEmail()
        
