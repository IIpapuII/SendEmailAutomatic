from components.dataExtract import extracJSON
from components.dataExtract import extracJSON


def textExtraction():
    dataJSON = extracJSON('kccparreto.json')

    for i in dataJSON:
        if str(i).count('Z') > 0:
            print('gran')
        else:
            print('gelvez')

    print(i.find('z'))