from components.sendMail import sendMailEcxel
from generator.seriesGeneration import SeriesInvoiceSend
from components.transformData import exportHTML, dateNowFormat
from components.dataExtract import getFilePath, extracJSON


def sendSeriesInvoiceCurrent():
    """ Modulo se encarga de generar el vencimiento de las series de documentos  SAP """

    dataJSON = extracJSON('counter.json')
    #Control de Lectura
    for i in dataJSON:
        print(i)
        container = SeriesInvoiceSend(schemeDB= dataJSON[i]['ShemeDB'],
            codeHouse= dataJSON[i]['codeHouse'],
            nameHouse= dataJSON[i]['nameHouse'])
        data, names = container.transformData()
        triggerMail = sendMailEcxel(
            dataJSON[i]['sender'],
            dataJSON[i]['addresse'],
            "Serie de Facturas y Fechas de Vencimiento".format(dataJSON[i]['nameHouse'],dateNowFormat()),
            exportHTML('seriesNotification.html', date_today = dateNowFormat(),
                       header = names, dataSeries = data, 
                       distributor_entity = dataJSON[i]['nameHouse']),None, password= dataJSON[i]['password']
            )
        
        for fields in range(len(data)):
            row = data[fields]
            if row[1] > 500 or row[2] > 3:
                print("No fue enviado el mensaje")
            else:
                triggerMail.sendProviderEmail()
                break
        