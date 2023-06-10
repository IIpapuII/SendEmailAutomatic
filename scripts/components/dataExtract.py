from model.conectDB import conect
from .transformData import ExtractDescription
import json, os

#SQL data extraction component using string query
def extracData(text):
    coon = conect()
    coon.execute(text)
    return coon.fetchall() , ExtractDescription(coon.description)

def extracJSON(NameArchive):
    dataJSON = open(os.path.join(os.path.dirname(os.path.abspath('config')),'scripts/config/'+ NameArchive), "r")
    dataJSON = json.loads(str(dataJSON.read()))
    return dataJSON