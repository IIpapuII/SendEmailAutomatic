import pandas as pd
import os 
from datetime import datetime
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
    date = datetime.now()
    return date.strftime("%Y%m%d")

def dateNowFormat():
    date = datetime.now()
    return date.strftime("%m/%d/%Y")

def exportHTML(nameArchive, **vars):
    loader = FileSystemLoader('scripts/templates')
    env = Environment(loader= loader)
    template = env.get_template(nameArchive)
    body = template.render(**vars)
    return body

def convertNumberToText(numero):
    texto = num2words(numero, lang='es')
    return texto

def formatNumberMoney(number_str = str):
    floatq = number_str.find(".")
    number_str_len = len(number_str)
    number = float(number_str)

    coin = "${:,.2f}".format(number).replace(",","n").replace(".",",").replace("n",".")

    if floatq == -1:
        num_separated = [int(a) for a in number_str]
        num_lim = num_separated[-6:]
    else:
        number_str_wdot = number_str.replace(".","")
        num_separated = [int(a) for a in number_str_wdot]
        num_lim = num_separated[-8:]

    parameter = 0

    for a in range(len(num_lim)):
        parameter = parameter + num_lim[a]

    if parameter == 0:
        ref = "de pesos"
    else:
        ref = "pesos"
    return coin, ref