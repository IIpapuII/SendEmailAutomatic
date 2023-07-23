import pandas as pd
import os 
from datetime import datetime
import datetime as td
from jinja2 import Environment, FileSystemLoader
from num2words import num2words

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
    "Fecha actual para formato SQL HANA"
    date = datetime.now()
    return date.strftime("%Y%m%d")

def dateFirstDay():
    "Fecha del primer dia del mes SQL HANA"
    dateNow = td.date.today()
    firstDay = dateNow.replace(day= 1)
    return firstDay.strftime("%Y%m%d")

def dateNowFormat():
    date = datetime.now()
    return date.strftime("%m/%d/%Y")

def exportHTML(nameArchive, **vars):
    currentDir = os.path.dirname(os.path.abspath(__file__))
    templateDir = os.path.join(currentDir,'..',"templates")
    print(templateDir)
    loader = FileSystemLoader(templateDir)
    env = Environment(loader= loader)
    template = env.get_template(nameArchive)
    body = template.render(**vars)
    return body

def convertNumberToText(numero):
    texto = num2words(numero, lang='es')
    return texto

def formatNumberMoney(number_str: str):
    number_str = str(number_str)
    number_int = int(number_str)
    parameter = 0

    coin = "${:,.2f}".format(number_int).replace(",","n").replace(".",",").replace("n",".")

    num_separated = [a for a in number_str]

    if len(num_separated) <= 6:
        ref = "pesos"
    else:
        num_lim = num_separated[-6:]

        for a in range(len(num_lim)):
            parameter = parameter + int(num_lim[a])

        if parameter == 0:
            ref = "de pesos"
        else:
            ref = "pesos"
            
    return coin, ref

def fromListToString (variable: str):
    newVariable = variable.replace("[","").replace("]","")
    return newVariable