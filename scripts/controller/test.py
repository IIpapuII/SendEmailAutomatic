from generator.parrettoGeneration import ParrettoSend
from components.dataExtract import extracJSON

def textExtraction():
    dataJSON = extracJSON('supplier.json')
    list_key = []

    for key in dataJSON:
        list_key.append(key)
        
    print(list_key)