from components.sendMail import sendMailEcxel
from generator.seriesGeneration import SeriesInvoiceSend
from components.transformData import exportHTML, dateNowFormat
from components.dataExtract import extracJSON


def sendSeriesInvoiceCurrent():
    """ Modulo se encarga de generar el vencimiento de las series de documentos SAP """

    dataJSON = extracJSON('counter.json')
    #Control de Lectura
    for title in dataJSON:
        print(title)
        container = SeriesInvoiceSend(schemeDB= dataJSON[title]['schemeDB'], table= dataJSON[title]['table'])
        datas, names = container.transformData()

        triggerMail = sendMailEcxel(
            dataJSON[title]['sender'],
            dataJSON[title]['sender'], #dataJSON[title]['addresse'],
            title,
            exportHTML('seriesNotification.html', date_today = dateNowFormat(),
                       header = names, dataSeries = datas, 
                       distributor_entity = dataJSON[title]['nameHouse'],
                       text = dataJSON[title]['text']),
            None, 
            password= dataJSON[title]['password']
            )
        
        for fields in datas:
            if fields[1] > 500 and fields[2] > 3:
                print(fields, " - en regla")
            else:
                triggerMail.sendProviderEmail()
                break
        