import pandas as pd
import os 
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

#SQL description extraction function
def ExtractDescription(DataDescription: list) -> list:
    frameData = []
    for i in range(len(pd.array(DataDescription))):
        frameData.append(DataDescription[i][0])
    return frameData


def dataFusion(DataFrame, dataDescription):
    frameData = pd.DataFrame(DataFrame, columns= dataDescription )
    return frameData


def passArray(Data):
    DatosConvert = []
    for i in Data:
        for j in i:
            DatosConvert.append(str(j))
    return DatosConvert


def exportExcel(dataFrame, NameArchive):
    pd.DataFrame(dataFrame).to_excel(os.path.join(os.path.dirname(os.path.abspath('docs')),'scripts/docs/'+ NameArchive))


def dateNowPC():
    date = datetime.now()
    return date.strftime("%d/%m/%Y")

def dateNowHana():
    date = datetime.now()
    return date.strftime("%Y%m%d")

def exportHTML(nameArchive):
    loader = FileSystemLoader('scripts/templates')
    env = Environment(loader= loader)
    template = env.get_template(nameArchive)
    body = template.render()
    return body

