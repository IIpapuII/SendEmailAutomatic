from components.sendMail import sendMailEcxel
from generator.parrettoGeneration import ParrettoSend
from components.transformData import exportHTML, dateNowFormat
from components.dataExtract import extracJSON


def sendParrettoCurrent():
    """ Modulo Encargado de Gestionar la lectura del Json Junto con el Envio de los archivos Generados """

    dataJSON = extracJSON('parreto.json')
    for i in dataJSON:
        print(i)
        triggerData = ParrettoSend (schemeDB= dataJSON[i]['schemeDB'], wareHouse= dataJSON[i]['WareHouse'])
        
        triggerMail = sendMailEcxel(
            dataJSON[i]['sender'],
            "supporsistemas@c.gelvezdistribuciones.com",
            "Sabana de Ventas para Liquidaciones," + dateNowFormat(),
            exportHTML('massiveParretto.html', date_today = dateNowFormat(), distributor_entity = dataJSON[i]['nameHouse']),
            'Parretto de Ventas.xlsx',
            dataJSON[i]['password']
            )
        triggerData.transformData()
        print('Se Genero: Sabana de ventas')
        triggerMail.sendProviderEmail()
        
