from generator.projectAccountingGenerate import ProjectAccountingEjecute
from components.dataExtract import extracJSON
from components.transformData import dateNowHana


def ejecuteProjectAccounting():

    dataJSON = extracJSON('Accounting.json')

    for i in dataJSON:
        triggerData = ProjectAccountingEjecute(
            dataJSON[i]['ShemeDB'],
            dateNowHana(),
            dateNowHana()
        )
        print(dataJSON[i]['ShemeDB'])
    
        triggerData.transformData()