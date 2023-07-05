from model.conectDB import conect
from .transformData import ExtractDescription
import json, os

def getFilePath(folderName, fileName):
    """Relative path modeler"""
    currentDir = os.path.dirname(os.path.abspath(__file__))
    filePath = os.path.join(currentDir,'..', folderName, fileName)
    return filePath

#SQL data extraction component using string query
def extracData(text):
    coon = conect()
    coon.execute(text)
    return coon.fetchall() , ExtractDescription(coon.description)

def extracJSON(NameArchive):
    dataJSON = open(getFilePath('config', NameArchive), "r")
    dataJSON = json.loads(str(dataJSON.read()))
    return dataJSON