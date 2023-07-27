from datetime import datetime
from components.transformData import dateNowFormat
from components.dataExtract import extracJSON


def textExtraction():
    dataJSON = extracJSON('suppliers.json')   #Si es 15vo, se escojera json de supervisores
    listDefinition = []
    listWord = []
        
    for origin in dataJSON:  #Seleccionamos proveedor/supervisor

        print(datetime.now().day)