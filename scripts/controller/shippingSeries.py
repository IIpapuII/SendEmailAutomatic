from components.sendMail import sendMailEcxel
from generator.seriesGeneration import SeriesInvoiceSend
from components.transformData import exportHTML, dateNowFormat
from components.dataExtract import extracJSON


def sendSeriesInvoiceCurrent():
    """ Modulo se encarga de generar el vencimiento de las series de documentos  SAP """

    dataJSON = extracJSON('counter.json')
    #Control de Lectura
    for i in dataJSON:
        print(i)
        container = SeriesInvoiceSend(schemeDB= dataJSON[i]['schemeDB'])
        datas, names = container.transformData()

        triggerMail = sendMailEcxel(
            dataJSON[i]['sender'],
            dataJSON[i]['addresse'],
            "Serie de Facturas y Fechas de Vencimiento",
            exportHTML('seriesNotification.html', date_today = dateNowFormat(),
                       header = names, dataSeries = datas, 
                       distributor_entity = dataJSON[i]['nameHouse']),
            None, 
            password= dataJSON[i]['password']
            )
        
        for fields in datas:
            if fields[1] > 500 and fields[2] > 3:
                print(fields, " - en regla")
            else:
                triggerMail.sendProviderEmail()
                break
        