from model.conectDB import conect
from .transformData import ExtractDescription
import json, os

def getFilePath(folderName, fileName):
    """Relative path modeler"""
    currentDir = os.path.dirname(os.path.abspath(__file__))
    filePath = os.path.join(currentDir,'..', folderName, fileName)
    return filePath

def getFilePathsEmail(folderName:str, fileNames:list):
    """Relative path modeler mutiple"""
    currentDir = os.path.dirname(os.path.abspath(__file__))
    filePaths = []
    for fileName in fileNames:
        filePath = os.path.join(currentDir,'..', folderName, fileName)
        filePaths.append(filePath)
    return filePaths

#SQL data extraction component using string query
def extracData(text):
    coon = conect()
    coon.execute(text)
    return coon.fetchall() , ExtractDescription(coon.description)

def ejecuteQueryNotDate(text):
    coon = conect()
    coon.execute(text)

def extracJSON(NameArchive):
    """Ingresar el nombre del archivo Json a leer y traduccir"""
    dataJSON: dict = open(getFilePath('config', NameArchive), "r")
    dataJSON = json.loads(str(dataJSON.read()))
    return dataJSON