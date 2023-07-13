from generator.projectAccountingGenerate import ProjectAccountingEjecute
from components.dataExtract import extracJSON
from components.transformData import dateNowHana, dateFirstDay


def ejecuteProjectAccounting():

    dataJSON = extracJSON('Accounting.json')

    for i in dataJSON:
        triggerData = ProjectAccountingEjecute(
            dataJSON[i]['schemeDB'],
            dateNowHana(),
            dateNowHana()
        )
    
    triggerData.transformData()