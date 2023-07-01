from components.sendMail import sendMailEcxel
from generator.seriesGeneration import SeriesInvoiceSend
from components.transformData import exportHTML, dateNowFormat
import json
import os
import jinja2

def sendSeriesInvoiceCurrent():
    """ Modulo Encargado de Gestionar la lectura del Json Junto con el Envio de los archivos Generados """

    dataJSON = open(os.path.join(os.path.dirname(os.path.abspath('config')),'scripts/config/counter.json'), "r")
    dataJSON = json.loads(str(dataJSON.read()))

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
                       distributor_entity = dataJSON[i]['nameHouse']),None
            )
        for fields in range(len(data)):
            row = data[fields]
            if row[1] > 1000 and row[2] > 10:
                print("No fue enviado el mensaje")
            else:
                triggerMail.sendProviderEmail()
                break
        